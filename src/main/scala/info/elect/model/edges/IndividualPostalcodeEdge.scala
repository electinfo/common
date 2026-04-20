// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Individual)-[:IN_ZIP]->(PostalCode) */
object IndividualPostalcodeEdge extends SchemaBase {

  val tableName = "individual_postalcode_edges"
  val relType = "IN_ZIP"
  val srcLabel = "Individual"
  val dstLabel = "PostalCode"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("cycles")))
}
