// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:RAN_IN_CYCLE]->(Cycle) */
object CandidateCycleEdge extends SchemaBase {

  val tableName = "candidate_cycle_edges"
  val relType = "RAN_IN_CYCLE"
  val srcLabel = "Candidate"
  val dstLabel = "Cycle"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("fec_candidate_id"),
      opt("cycle_year", IntegerType),
      opt("election_year", IntegerType),
      opt("office"),
      opt("office_state"),
      opt("office_district"),
      opt("incumbent_challenger_status"),
      opt("candidate_status"),
      opt("party_affiliation")))
}
