// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Congressional and state legislative districts */
object DistrictEntity extends SchemaBase {

  val tableName = "district_entities"
  val label = "District"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      opt("state"),
      opt("district_number"),
      opt("district_type"),
      opt("geoid"),
      opt("geoid_cd"),
      opt("name"),
      opt("district_slug"),
      opt("land_area_sqmi", DoubleType),
      opt("water_area_sqmi", DoubleType)))
}
