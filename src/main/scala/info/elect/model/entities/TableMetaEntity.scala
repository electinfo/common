// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Meta-entity representing a quicksilver table within a catalog */
object TableMetaEntity extends SchemaBase {

  val tableName = "table_meta_entities"
  val label = "TableMeta"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("tier"),
      req("table_name"),
      opt("row_count", LongType),
      opt("column_count", IntegerType),
      opt("duplicate_ids", LongType),
      opt("incatalog_orphan_src_count", LongType),
      opt("incatalog_orphan_src_pct", DoubleType),
      opt("incatalog_orphan_dst_count", LongType),
      opt("incatalog_orphan_dst_pct", DoubleType),
      opt("crosscatalog_orphan_src_count", LongType),
      opt("crosscatalog_orphan_src_pct", DoubleType),
      opt("crosscatalog_orphan_dst_count", LongType),
      opt("crosscatalog_orphan_dst_pct", DoubleType),
      opt("table_type")))
}
