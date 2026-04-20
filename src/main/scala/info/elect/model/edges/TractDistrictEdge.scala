// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Tract)-[:OVERLAPS]->(District) */
object TractDistrictEdge extends SchemaBase {

  val tableName = "tract_district_edges"
  val relType = "OVERLAPS"
  val srcLabel = "Tract"
  val dstLabel = "District"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("overlap_land_area", LongType)))
}
