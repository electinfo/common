// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Committee)-[:SUPPORTS]->(Candidate) */
object CommitteeCandidateEdge extends SchemaBase {

  val tableName = "committee_candidate_edges"
  val relType = "SUPPORTS"
  val srcLabel = "Committee"
  val dstLabel = "Candidate"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("committee_name"),
      opt("candidate_name"),
      opt("state"),
      opt("jurisdiction")))
}
