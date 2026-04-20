// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Race)-[:IN_STATE]->(State) */
object RaceStateEdge extends SchemaBase {

  val tableName = "race_state_edges"
  val relType = "IN_STATE"
  val srcLabel = "Race"
  val dstLabel = "State"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("state"),
      opt("election_year", IntegerType)))
}
