// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Aggregate candidate stats per office (does not use standard entityBase) */
object OfficeCandidateStats extends SchemaBase {

  val tableName = "office_candidate_stats"
  val label = "OfficeCandidateStats"

  val schema: StructType = StructType(
    Seq(
      opt(ORIGIN_CATALOG),
      req("office_id"),
      req("candidate_count", LongType),
      opt("election_years"),
      opt("active_cycles")))
}
