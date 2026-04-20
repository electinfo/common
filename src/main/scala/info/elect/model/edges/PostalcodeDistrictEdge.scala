// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (PostalCode)-[:OVERLAPS]->(District) */
object PostalcodeDistrictEdge extends SchemaBase {

  val tableName = "postalcode_district_edges"
  val relType = "OVERLAPS"
  val srcLabel = "PostalCode"
  val dstLabel = "District"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("overlap_land_area", LongType),
      opt("overlap_water_area", LongType)))
}
