// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Individual)-[:RESIDES_IN]->(Place) */
object IndividualPlaceEdge extends SchemaBase {

  val tableName = "individual_place_edges"
  val relType = "RESIDES_IN"
  val srcLabel = "Individual"
  val dstLabel = "Place"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("cycles")))
}
