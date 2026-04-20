// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:AFFILIATED_WITH]->(Party) */
object CandidatePartyEdge extends SchemaBase {

  val tableName = "candidate_party_edges"
  val relType = "AFFILIATED_WITH"
  val srcLabel = "Candidate"
  val dstLabel = "Party"

  val schema: StructType = StructType(edgeBase)
}
