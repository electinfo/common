// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Census blocks with voter registration and turnout data */
object BlockEntity extends SchemaBase {

  val tableName = "block_entities"
  val label = "Block"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("geoid"),
      opt("state_fips"),
      opt("county_fips"),
      opt("geoid_county"),
      opt("tract"),
      opt("block"),
      opt("state"),
      opt("reg_total", LongType),
      opt("reg_dem", LongType),
      opt("reg_rep", LongType),
      opt("reg_ind", LongType),
      opt("reg_oth", LongType),
      opt("reg_male", LongType),
      opt("reg_female", LongType),
      opt("reg_white", LongType),
      opt("reg_hispanic", LongType),
      opt("reg_black", LongType),
      opt("reg_asian", LongType),
      opt("gen2022_voted", LongType),
      opt("gen2022_turnout_pct", DoubleType),
      opt("gen2022_voted_white", LongType),
      opt("gen2022_voted_hispanic", LongType),
      opt("gen2022_voted_black", LongType),
      opt("gen2022_voted_asian", LongType),
      opt("gen2022_turnout_pct_white", DoubleType),
      opt("gen2022_turnout_pct_hispanic", DoubleType),
      opt("gen2022_turnout_pct_black", DoubleType),
      opt("gen2022_turnout_pct_asian", DoubleType),
      opt("gen2022_voted_male", LongType),
      opt("gen2022_voted_female", LongType),
      opt("gen2022_turnout_pct_male", DoubleType),
      opt("gen2022_turnout_pct_female", DoubleType)))
}
