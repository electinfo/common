// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Officeholder)-[:HELD]->(Office) */
object OfficeholderOfficeEdge extends SchemaBase {

  val tableName = "officeholder_office_edges"
  val relType = "HELD"
  val srcLabel = "Officeholder"
  val dstLabel = "Office"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("office_type"),
      opt("state"),
      opt("district"),
      opt("party"),
      opt("election_year", IntegerType)))
}
