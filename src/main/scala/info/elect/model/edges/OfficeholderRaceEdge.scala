// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Officeholder)-[:COMPETED_IN]->(Race) */
object OfficeholderRaceEdge extends SchemaBase {

  val tableName = "officeholder_race_edges"
  val relType = "COMPETED_IN"
  val srcLabel = "Officeholder"
  val dstLabel = "Race"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("bioguide_id"),
      opt("election_year", IntegerType),
      opt("congress", LongType),
      opt("party")))
}
