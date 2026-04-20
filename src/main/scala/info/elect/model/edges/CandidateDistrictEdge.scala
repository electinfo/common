// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:IN_DISTRICT]->(District) */
object CandidateDistrictEdge extends SchemaBase {

  val tableName = "candidate_district_edges"
  val relType = "IN_DISTRICT"
  val srcLabel = "Candidate"
  val dstLabel = "District"

  val schema: StructType = StructType(edgeBase)
}
