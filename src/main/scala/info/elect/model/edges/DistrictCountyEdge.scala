// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (District)-[:OVERLAPS]->(County) */
object DistrictCountyEdge extends SchemaBase {

  val tableName = "district_county_edges"
  val relType = "OVERLAPS"
  val srcLabel = "District"
  val dstLabel = "County"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("overlap_land_area", LongType),
      opt("overlap_water_area", LongType)))
}
