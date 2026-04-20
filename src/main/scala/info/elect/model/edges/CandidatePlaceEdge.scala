// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:IN_PLACE]->(Place) */
object CandidatePlaceEdge extends SchemaBase {

  val tableName = "candidate_place_edges"
  val relType = "IN_PLACE"
  val srcLabel = "Candidate"
  val dstLabel = "Place"

  val schema: StructType = StructType(edgeBase)
}
