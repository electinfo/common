// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Race)-[:FOR_OFFICE]->(Office) */
object RaceOfficeEdge extends SchemaBase {

  val tableName = "race_office_edges"
  val relType = "FOR_OFFICE"
  val srcLabel = "Race"
  val dstLabel = "Office"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("office_type"),
      opt("state"),
      opt("district")))
}
