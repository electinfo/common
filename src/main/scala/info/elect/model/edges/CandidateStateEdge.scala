// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:IN_STATE]->(State) */
object CandidateStateEdge extends SchemaBase {

  val tableName = "candidate_state_edges"
  val relType = "IN_STATE"
  val srcLabel = "Candidate"
  val dstLabel = "State"

  val schema: StructType = StructType(edgeBase)
}
