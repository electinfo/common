// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:COMPETED_IN]->(Race) */
object CandidateRaceEdge extends SchemaBase {

  val tableName = "candidate_race_edges"
  val relType = "COMPETED_IN"
  val srcLabel = "Candidate"
  val dstLabel = "Race"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("bioguide_id"),
      opt("election_year", IntegerType),
      opt("congress", LongType)))
}
