// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:IN_ZIP]->(PostalCode) */
object CandidateZipEdge extends SchemaBase {

  val tableName = "candidate_zip_edges"
  val relType = "IN_ZIP"
  val srcLabel = "Candidate"
  val dstLabel = "PostalCode"

  val schema: StructType = StructType(edgeBase)
}
