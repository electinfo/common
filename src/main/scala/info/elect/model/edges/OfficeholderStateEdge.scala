// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Officeholder)-[:REPRESENTED]->(State) */
object OfficeholderStateEdge extends SchemaBase {

  val tableName = "officeholder_state_edges"
  val relType = "REPRESENTED"
  val srcLabel = "Officeholder"
  val dstLabel = "State"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("bioguide_id"),
      opt("congresses"),
      opt("party"),
      opt("start_year"),
      opt("end_year")))
}
