// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Census places (cities, towns, CDPs) */
object PlaceEntity extends SchemaBase {

  val tableName = "place_entities"
  val label = "Place"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("state"),
      opt("state_fips"),
      opt("place_fips"),
      opt("geoid"),
      opt("name_normalized"),
      opt("lsad"),
      opt("latitude", DoubleType),
      opt("longitude", DoubleType),
      opt("land_area_sqmi", DoubleType),
      opt("water_area_sqmi", DoubleType)))
}
