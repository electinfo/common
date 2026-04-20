// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (CatalogMeta)-[:HAS_TABLE]->(TableMeta) */
object CatalogTableEdge extends SchemaBase {

  val tableName = "catalog_table_edges"
  val relType = "HAS_TABLE"
  val srcLabel = "CatalogMeta"
  val dstLabel = "TableMeta"

  val schema: StructType = StructType(edgeBase)
}
