// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Name-match vertices for candidate entity resolution */
object CandidateNameVertex extends SchemaBase {

  val tableName = "candidate_name_vertices"
  val label = "CandidateNameVertex"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name_field"),
      req("normalized_value"),
      opt("candidate_count", LongType),
      opt("catalog_count", LongType)))
}
