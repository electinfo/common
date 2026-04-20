// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType, TimestampType}
import info.elect.model.SchemaBase

/** Political candidates across all jurisdictions */
object CandidateEntity extends SchemaBase {

  val tableName = "candidate_entities"
  val label = "Candidate"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("full_name"),
      opt("full_name_normalized"),
      opt("first_name"),
      opt("last_name"),
      opt("middle_name"),
      opt("name_suffix"),
      opt("city"),
      opt("state"),
      opt("zip"),
      opt("county"),
      opt("office"),
      opt("office_state"),
      opt("office_district"),
      opt("office_code"),
      opt("office_desc"),
      opt("district"),
      opt("jurisdiction"),
      opt("seek_office"),
      opt("seek_office_district"),
      opt("seek_office_descr"),
      opt("hold_office"),
      opt("hold_office_district"),
      opt("hold_office_descr"),
      opt("incumbent_challenger_status"),
      opt("candidate_status"),
      opt("candidate_type"),
      opt("status"),
      opt("status_code"),
      opt("status_desc"),
      opt("principal_campaign_committee"),
      opt("fec_candidate_id"),
      opt("tec_filer_id"),
      opt("fl_doe_acct_num"),
      opt("az_sos_candidate_id"),
      opt("wa_pdc_filer_id"),
      opt("me_ethics_org_id"),
      opt("ca_fppc_filer_id"),
      opt("oh_sos_master_key"),
      opt("bioguide_id"),
      opt("is_current"),
      opt("portrait_url"),
      opt("most_recent_state"),
      opt("most_recent_chamber"),
      opt("eff_start_dt", TimestampType),
      opt("eff_stop_dt", TimestampType)))
}
