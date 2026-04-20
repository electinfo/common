// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** ZIP code tabulation areas */
object PostalcodeEntity extends SchemaBase {

  val tableName = "postalcode_entities"
  val label = "PostalCode"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("zip_code"),
      opt("state"),
      opt("geoid"),
      opt("land_area_m2", LongType),
      opt("water_area_m2", LongType),
      opt("district_count", LongType)))
}
