// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:HAS_NAME]->(CandidateNameVertex) */
object CandidateNameEdge extends SchemaBase {

  val tableName = "candidate_name_edges"
  val relType = "HAS_NAME"
  val srcLabel = "Candidate"
  val dstLabel = "CandidateNameVertex"

  val schema: StructType = StructType(edgeBase)
}
