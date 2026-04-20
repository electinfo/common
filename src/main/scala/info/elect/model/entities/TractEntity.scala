// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Census tracts with demographic/economic data */
object TractEntity extends SchemaBase {

  val tableName = "tract_entities"
  val label = "Tract"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      opt("state"),
      opt("county"),
      opt("tract"),
      opt("geoid"),
      opt("name"),
      opt("state_fips"),
      opt("county_fips"),
      opt("total_population", IntegerType),
      opt("total_population_moe", IntegerType),
      opt("median_household_income", IntegerType),
      opt("median_household_income_moe", IntegerType),
      opt("median_home_value", IntegerType),
      opt("median_gross_rent", IntegerType),
      opt("total_housing_units", IntegerType),
      opt("pop_white", IntegerType),
      opt("pop_black", IntegerType),
      opt("pop_asian", IntegerType),
      opt("pop_hispanic", IntegerType),
      opt("pop_below_poverty", IntegerType),
      opt("poverty_rate", DoubleType),
      opt("pop_hs_diploma", IntegerType),
      opt("hs_diploma_pct", DoubleType),
      opt("bachelors_plus", LongType),
      opt("bachelors_plus_pct", DoubleType),
      opt("insured_pct", DoubleType),
      opt("drove_alone_pct", DoubleType),
      opt("public_transit_pct", DoubleType),
      opt("work_from_home_pct", DoubleType)))
}
