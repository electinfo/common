// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** US counties */
object CountyEntity extends SchemaBase {

  val tableName = "county_entities"
  val label = "County"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("state"),
      opt("state_fips"),
      opt("county_fips"),
      opt("geoid"),
      opt("latitude", DoubleType),
      opt("longitude", DoubleType),
      opt("land_area_sqmi", DoubleType),
      opt("water_area_sqmi", DoubleType)))
}
