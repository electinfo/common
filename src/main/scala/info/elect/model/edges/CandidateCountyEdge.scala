// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:IN_COUNTY]->(County) */
object CandidateCountyEdge extends SchemaBase {

  val tableName = "candidate_county_edges"
  val relType = "IN_COUNTY"
  val srcLabel = "Candidate"
  val dstLabel = "County"

  val schema: StructType = StructType(edgeBase)
}
