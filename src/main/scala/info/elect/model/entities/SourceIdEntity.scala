// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Source-specific identifier entities for cross-catalog resolution */
object SourceIdEntity extends SchemaBase {

  val tableName = "source_id_entities"
  val label = "SourceId"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("id_type"),
      req("id_value"),
      opt("candidate_count", LongType),
      opt("catalog_count", LongType)))
}
