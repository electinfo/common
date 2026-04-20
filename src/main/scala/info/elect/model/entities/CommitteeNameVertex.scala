// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Name-match vertices for committee entity resolution */
object CommitteeNameVertex extends SchemaBase {

  val tableName = "committee_name_vertices"
  val label = "CommitteeNameVertex"

  val schema: StructType = StructType(entityBase ++ Seq(req("normalized_name"), opt("committee_count", LongType), opt("catalog_count", LongType)))
}
