// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, DoubleType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (TableMeta)-[:HAS_FIELD]->(FieldMeta) */
object TableFieldEdge extends SchemaBase {

  val tableName = "table_field_edges"
  val relType = "HAS_FIELD"
  val srcLabel = "TableMeta"
  val dstLabel = "FieldMeta"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("with_value", LongType),
      opt("null_value", LongType),
      opt("distinct_count", LongType),
      opt("fill_rate", DoubleType)))
}
