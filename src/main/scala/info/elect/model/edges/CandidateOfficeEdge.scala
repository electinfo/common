// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:RAN_FOR]->(Office) */
object CandidateOfficeEdge extends SchemaBase {

  val tableName = "candidate_office_edges"
  val relType = "RAN_FOR"
  val srcLabel = "Candidate"
  val dstLabel = "Office"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("fec_candidate_id"),
      opt("election_year", IntegerType),
      opt("incumbent_challenger_status"),
      opt("candidate_status"),
      opt("cycle", IntegerType),
      opt("bioguide_id"),
      opt("office_type"),
      opt("state"),
      opt("district")))
}
