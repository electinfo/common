#!/usr/bin/env node
/**
 * Generates Scala source files from quicksilver-metamodel.json.
 *
 * Output structure:
 *   src/main/scala/info/elect/model/
 *     SchemaBase.scala              - req/opt helpers + base sequences
 *     QuicksilverSchemas.scala      - registry + utilities (backward-compat)
 *     entities/<Name>Entity.scala   - one per entity type
 *     edges/<Name>Edge.scala        - one per edge type
 *
 * Usage:
 *   node scripts/generate-model.js [--check]
 *
 *   --check   Verify generated files are up-to-date (exits non-zero if stale)
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = path.resolve(__dirname, "..");
const SCHEMA_PATH = path.join(ROOT, "schemas", "quicksilver-metamodel.json");
const OUTPUT_BASE = path.join(ROOT, "src", "main", "scala", "info", "elect", "model");

// ============================================================================
//  Load metamodel
// ============================================================================

const model = JSON.parse(fs.readFileSync(SCHEMA_PATH, "utf8"));
const defs = model["$defs"];
const registryOrder = model["x-registry-order"] || [];
const resolutionRules = model["x-resolution-rules"] || [];

// ============================================================================
//  Type resolution
// ============================================================================

function sparkType(propSchema) {
  if (propSchema["x-spark-type"]) return propSchema["x-spark-type"];
  const t = propSchema.type || "string";
  const fmt = propSchema.format;
  if (t === "string") {
    if (fmt === "date") return "DateType";
    if (fmt === "date-time") return "TimestampType";
    return "StringType";
  }
  if (t === "integer") return "IntegerType";
  if (t === "number") return "DoubleType";
  if (t === "boolean") return "BooleanType";
  return "StringType";
}

// ============================================================================
//  Naming helpers
// ============================================================================

function toCamelCase(snake) {
  const parts = snake.split("_");
  return parts[0] + parts.slice(1).map(p => p.charAt(0).toUpperCase() + p.slice(1)).join("");
}

function toPascalCase(snake) {
  return snake.split("_").map(p => p.charAt(0).toUpperCase() + p.slice(1)).join("");
}

// Entity table name -> object name: "candidate_entities" -> "CandidateEntity"
function entityObjectName(tableName) {
  // Remove trailing 's' from entities/vertices/stats
  let name = toPascalCase(tableName);
  if (name.endsWith("Entities")) name = name.slice(0, -8) + "Entity";
  else if (name.endsWith("Vertices")) name = name.slice(0, -8) + "Vertex";
  else if (name.endsWith("Stats")) name = name; // keep as-is
  return name;
}

// Edge table name -> object name: "individual_committee_edges" -> "IndividualCommitteeEdge"
function edgeObjectName(tableName) {
  let name = toPascalCase(tableName);
  if (name.endsWith("Edges")) name = name.slice(0, -5) + "Edge";
  return name;
}

// ============================================================================
//  Scala field rendering
// ============================================================================

function scalaField(name, propSchema, isRequired) {
  const fn = isRequired ? "req" : "opt";
  const st = sparkType(propSchema);
  if (st === "StringType") return `${fn}("${name}")`;
  return `${fn}("${name}", ${st})`;
}

// ============================================================================
//  File generation
// ============================================================================

const generatedFiles = new Map(); // path -> content

function header(pkg) {
  return `// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package ${pkg}
`;
}

// --- SchemaBase.scala ---
function generateSchemaBase() {
  const entityBaseProps = defs.entityBase.properties;
  const entityBaseRequired = new Set(defs.entityBase.required || []);
  const edgeBaseProps = defs.edgeBase.properties;
  const edgeBaseRequired = new Set(defs.edgeBase.required || []);

  const ebParts = Object.keys(entityBaseProps).map(name => {
    if (name === "catalog") return 'opt(ORIGIN_CATALOG)';
    const fn = entityBaseRequired.has(name) ? "req" : "opt";
    return `${fn}("${name}")`;
  });

  const edbParts = Object.keys(edgeBaseProps).map(name => {
    if (name === "catalog") return 'opt(ORIGIN_CATALOG)';
    const fn = edgeBaseRequired.has(name) ? "req" : "opt";
    return `${fn}("${name}")`;
  });

  return `${header("info.elect.model")}
import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}

/**
 * Shared helpers and base column sequences for quicksilver schemas.
 * Entity and edge objects extend this to inherit req/opt builders and base columns.
 */
trait SchemaBase {

  val ORIGIN_CATALOG = "catalog"

  /** Required column -- source must provide this. */
  protected def req(name: String, dt: DataType = StringType): StructField =
    StructField(name, dt, nullable = false)

  /** Optional column -- null-filled if source doesn't have it. */
  protected def opt(name: String, dt: DataType = StringType): StructField =
    StructField(name, dt, nullable = true)

  protected val entityBase: Seq[StructField] = Seq(${ebParts.join(", ")})

  protected val edgeBase: Seq[StructField] = Seq(${edbParts.join(", ")})
}

object SchemaBase extends SchemaBase
`;
}

// --- Individual entity file ---
function generateEntityFile(tableName, schema) {
  const objName = entityObjectName(tableName);
  const label = schema["x-label"] || objName;
  const desc = schema["x-description"] || "";
  const props = schema.properties || {};
  const required = new Set(schema.required || []);
  const hasBaseOverride = schema["x-base-override"] || false;

  const baseEntityFields = new Set(Object.keys(defs.entityBase.properties));

  // Determine which Spark types are needed for imports
  const sparkTypes = new Set(["StringType", "StructField", "StructType"]);
  for (const [pname, pschema] of Object.entries(props)) {
    if (!hasBaseOverride && baseEntityFields.has(pname)) continue;
    sparkTypes.add(sparkType(pschema));
  }
  // Always need DataType for the trait
  sparkTypes.add("DataType");

  const sortedImports = [...sparkTypes].sort();

  let fieldLines;
  if (hasBaseOverride) {
    // All fields are explicit (no entityBase prefix)
    fieldLines = Object.entries(props).map(([pname, pschema]) => {
      if (pname === "catalog") return '      opt(ORIGIN_CATALOG)';
      return `      ${scalaField(pname, pschema, required.has(pname))}`;
    });
    const body = `  val schema: StructType = StructType(
    Seq(
${fieldLines.join(",\n")}))`;
    return `${header("info.elect.model.entities")}
import org.apache.spark.sql.types.{${sortedImports.join(", ")}}
import info.elect.model.SchemaBase

/** ${desc} */
object ${objName} extends SchemaBase {

  val tableName = "${tableName}"
  val label = "${label}"

${body}
}
`;
  } else {
    // Normal entity: entityBase ++ own fields
    const ownProps = Object.entries(props).filter(([k]) => !baseEntityFields.has(k));
    fieldLines = ownProps.map(([pname, pschema]) =>
      `      ${scalaField(pname, pschema, required.has(pname))}`
    );

    let body;
    if (fieldLines.length <= 3) {
      const inline = ownProps.map(([pname, pschema]) =>
        scalaField(pname, pschema, required.has(pname))
      ).join(", ");
      body = `  val schema: StructType = StructType(entityBase ++ Seq(${inline}))`;
    } else {
      body = `  val schema: StructType = StructType(
    entityBase ++ Seq(
${fieldLines.join(",\n")}))`;
    }

    return `${header("info.elect.model.entities")}
import org.apache.spark.sql.types.{${sortedImports.join(", ")}}
import info.elect.model.SchemaBase

/** ${desc} */
object ${objName} extends SchemaBase {

  val tableName = "${tableName}"
  val label = "${label}"

${body}
}
`;
  }
}

// --- Individual edge file ---
function generateEdgeFile(tableName, schema) {
  const objName = edgeObjectName(tableName);
  const relType = schema["x-rel-type"] || "UNKNOWN";
  const src = schema["x-src"] || "?";
  const dst = schema["x-dst"] || "?";

  const baseEdgeFields = new Set(Object.keys(defs.edgeBase.properties));
  const props = schema.properties || {};
  const required = new Set(schema.required || []);
  const ownProps = Object.entries(props).filter(([k]) => !baseEdgeFields.has(k));

  // Determine imports
  const sparkTypes = new Set(["StringType", "StructField", "StructType", "DataType"]);
  for (const [pname, pschema] of ownProps) {
    sparkTypes.add(sparkType(pschema));
  }
  const sortedImports = [...sparkTypes].sort();

  let body;
  if (ownProps.length === 0) {
    body = `  val schema: StructType = StructType(edgeBase)`;
  } else {
    const fieldLines = ownProps.map(([pname, pschema]) =>
      `      ${scalaField(pname, pschema, required.has(pname))}`
    );
    body = `  val schema: StructType = StructType(
    edgeBase ++ Seq(
${fieldLines.join(",\n")}))`;
  }

  return `${header("info.elect.model.edges")}
import org.apache.spark.sql.types.{${sortedImports.join(", ")}}
import info.elect.model.SchemaBase

/** (${src})-[:${relType}]->(${dst}) */
object ${objName} extends SchemaBase {

  val tableName = "${tableName}"
  val relType = "${relType}"
  val srcLabel = "${src}"
  val dstLabel = "${dst}"

${body}
}
`;
}

// --- QuicksilverSchemas.scala (backward-compat registry) ---
function generateRegistry() {
  const entities = Object.entries(defs).filter(([, v]) => v["x-kind"] === "entity");
  const edges = Object.entries(defs).filter(([, v]) => v["x-kind"] === "edge");

  const entityImports = entities.map(([tbl]) => `import info.elect.model.entities.${entityObjectName(tbl)}`);
  const edgeImports = edges.map(([tbl]) => `import info.elect.model.edges.${edgeObjectName(tbl)}`);

  // Registry entries in order
  const registryLines = registryOrder.map((tbl, i) => {
    const def_ = defs[tbl];
    if (!def_) return null;
    const kind = def_["x-kind"];
    const objName = kind === "entity" ? entityObjectName(tbl) : edgeObjectName(tbl);
    const comma = i < registryOrder.length - 1 ? "," : "";
    return `    "${tbl}" -> ${objName}.schema${comma}`;
  }).filter(Boolean);

  // Resolution rules
  let resolveBody = "";
  for (const rule of resolutionRules) {
    resolveBody += `      val civitechPattern = """${rule.pattern}""".r
      tableName match {
        case civitechPattern(suffix) =>
          val baseName = suffix match {
${Object.entries(rule.mappings).map(([s, t]) => `            case "${s}" => "${t}"`).join("\n")}
            case _ => None.orNull
          }
          if (baseName != null) registry.get(baseName) else None
        case _ => None
      }`;
  }

  return `${header("info.elect.model")}
import org.apache.spark.sql.types.{DataType, StructType}
${entityImports.join("\n")}
${edgeImports.join("\n")}

/**
 * Schema registry and utilities.
 * Individual schemas live in info.elect.model.entities.* and info.elect.model.edges.*.
 * This object provides the consolidated registry for lookup and validation.
 */
object QuicksilverSchemas extends SchemaBase {

  val registry: Map[String, StructType] = Map(
${registryLines.join("\n")}
  )

  /** Extract required column names from a canonical schema. */
  def requiredColumns(schema: StructType): Set[String] =
    schema.fields.filter(!_.nullable).map(_.name).toSet

  /** Extract all column names from a canonical schema. */
  def allColumns(schema: StructType): Set[String] =
    schema.fields.map(_.name).toSet

  /** Build a column name -> DataType map for a canonical schema. */
  def columnTypes(schema: StructType): Map[String, DataType] =
    schema.fields.map(f => f.name -> f.dataType).toMap

  /**
   * Resolve a table name to its canonical schema.
   * First tries exact match, then civitech per-state pattern.
   */
  def resolve(tableName: String): Option[StructType] = {
    registry.get(tableName).orElse {
${resolveBody}
    }
  }
}
`;
}

// ============================================================================
//  Main
// ============================================================================

function generate() {
  // SchemaBase
  generatedFiles.set(
    path.join(OUTPUT_BASE, "SchemaBase.scala"),
    generateSchemaBase()
  );

  // Entity files
  const entities = Object.entries(defs).filter(([, v]) => v["x-kind"] === "entity");
  for (const [tableName, schema] of entities) {
    const objName = entityObjectName(tableName);
    generatedFiles.set(
      path.join(OUTPUT_BASE, "entities", `${objName}.scala`),
      generateEntityFile(tableName, schema)
    );
  }

  // Edge files
  const edges = Object.entries(defs).filter(([, v]) => v["x-kind"] === "edge");
  for (const [tableName, schema] of edges) {
    const objName = edgeObjectName(tableName);
    generatedFiles.set(
      path.join(OUTPUT_BASE, "edges", `${objName}.scala`),
      generateEdgeFile(tableName, schema)
    );
  }

  // Registry
  generatedFiles.set(
    path.join(OUTPUT_BASE, "QuicksilverSchemas.scala"),
    generateRegistry()
  );
}

function writeAll() {
  for (const [filePath, content] of generatedFiles) {
    fs.mkdirSync(path.dirname(filePath), { recursive: true });
    fs.writeFileSync(filePath, content);
  }
  console.log(`Generated ${generatedFiles.size} files under ${path.relative(ROOT, OUTPUT_BASE)}/`);
}

function checkAll() {
  let stale = 0;
  for (const [filePath, content] of generatedFiles) {
    if (!fs.existsSync(filePath)) {
      console.error(`MISSING: ${path.relative(ROOT, filePath)}`);
      stale++;
    } else {
      const existing = fs.readFileSync(filePath, "utf8");
      if (existing !== content) {
        console.error(`STALE:   ${path.relative(ROOT, filePath)}`);
        stale++;
      }
    }
  }
  if (stale > 0) {
    console.error(`\n${stale} file(s) out of date. Run: npm run generate:scala`);
    process.exit(1);
  } else {
    console.log(`All ${generatedFiles.size} generated files are up-to-date.`);
  }
}

// Run
generate();

if (process.argv.includes("--check")) {
  checkAll();
} else {
  writeAll();
}
