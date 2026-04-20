// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Race)-[:IN_CYCLE]->(Cycle) */
object RaceCycleEdge extends SchemaBase {

  val tableName = "race_cycle_edges"
  val relType = "IN_CYCLE"
  val srcLabel = "Race"
  val dstLabel = "Cycle"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("election_year", IntegerType)))
}
