// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{BooleanType, DataType, DoubleType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Voting precincts with election results */
object PrecinctEntity extends SchemaBase {

  val tableName = "precinct_entities"
  val label = "Precinct"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      opt("geoid"),
      opt("state"),
      opt("state_fips"),
      opt("county_fips"),
      opt("precinct_id"),
      opt("votes_dem", IntegerType),
      opt("votes_rep", IntegerType),
      opt("votes_total", IntegerType),
      opt("pct_dem_lead", DoubleType),
      opt("official_boundary", BooleanType)))
}
