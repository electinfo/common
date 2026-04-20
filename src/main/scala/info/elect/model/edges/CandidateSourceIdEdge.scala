// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Candidate)-[:HAS_SOURCE_ID]->(SourceId) */
object CandidateSourceIdEdge extends SchemaBase {

  val tableName = "candidate_source_id_edges"
  val relType = "HAS_SOURCE_ID"
  val srcLabel = "Candidate"
  val dstLabel = "SourceId"

  val schema: StructType = StructType(edgeBase)
}
