// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType, TimestampType}
import info.elect.model.SchemaBase

/** Political committees (PACs, party committees, campaign committees) */
object CommitteeEntity extends SchemaBase {

  val tableName = "committee_entities"
  val label = "Committee"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("committee_name"),
      opt("committee_name_normalized"),
      opt("committee_type"),
      opt("committee_designation"),
      opt("committee_status"),
      opt("filer_type"),
      opt("persent_type"),
      opt("type_desc"),
      opt("treasurer_name"),
      opt("chair_name"),
      opt("party"),
      opt("party_affiliation"),
      opt("connected_org"),
      opt("candidate_id"),
      opt("city"),
      opt("state"),
      opt("zip"),
      opt("county"),
      opt("fec_committee_id"),
      opt("tec_filer_id"),
      opt("fl_doe_acct_num"),
      opt("az_sos_committee_id"),
      opt("wa_pdc_filer_id"),
      opt("me_ethics_org_id"),
      opt("ca_fppc_filer_id"),
      opt("oh_sos_master_key"),
      opt("eff_start_dt", TimestampType),
      opt("eff_stop_dt", TimestampType)))
}
