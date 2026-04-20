// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DoubleType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Registered voters (civitech, per-state) */
object VoterEntity extends SchemaBase {

  val tableName = "voter_entities"
  val label = "Voter"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      opt("civitech_voter_id"),
      opt("fips_state"),
      opt("fips_county"),
      opt("state"),
      opt("name_first"),
      opt("name_middle"),
      opt("name_last"),
      opt("name_suffix"),
      opt("name_first_display"),
      opt("name_last_display"),
      opt("dt_birth"),
      opt("age", IntegerType),
      opt("gender"),
      opt("race"),
      opt("party_id"),
      opt("registration_date"),
      opt("voter_status"),
      opt("sos_voter_status"),
      opt("city"),
      opt("addr_state"),
      opt("zip"),
      opt("latitude", DoubleType),
      opt("longitude", DoubleType),
      opt("county"),
      opt("congressional_district"),
      opt("state_senate_district"),
      opt("state_house_district"),
      opt("precinct"),
      opt("score_support_gen_dem", DoubleType),
      opt("score_turnout_presidential", DoubleType),
      opt("score_turnout_midterm", DoubleType),
      opt("first_vote_date"),
      opt("last_vote_date"),
      opt("total_votes", IntegerType),
      opt("dem_primary_votes", IntegerType),
      opt("rep_primary_votes", IntegerType)))
}
