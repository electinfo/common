// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:SAME_AS]->(Officeholder) */
object CandidateOfficeholderEdge extends SchemaBase {

  val tableName = "candidate_officeholder_edges"
  val relType = "SAME_AS"
  val srcLabel = "Candidate"
  val dstLabel = "Officeholder"

  val schema: StructType = StructType(edgeBase)
}
