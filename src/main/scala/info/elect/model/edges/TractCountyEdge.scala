// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Tract)-[:IN_COUNTY]->(County) */
object TractCountyEdge extends SchemaBase {

  val tableName = "tract_county_edges"
  val relType = "IN_COUNTY"
  val srcLabel = "Tract"
  val dstLabel = "County"

  val schema: StructType = StructType(edgeBase)
}
