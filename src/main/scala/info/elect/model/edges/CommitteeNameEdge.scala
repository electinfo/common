// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Committee)-[:HAS_NAME]->(CommitteeNameVertex) */
object CommitteeNameEdge extends SchemaBase {

  val tableName = "committee_name_edges"
  val relType = "HAS_NAME"
  val srcLabel = "Committee"
  val dstLabel = "CommitteeNameVertex"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("fec_committee_id"),
      opt("tec_filer_id"),
      opt("fl_doe_acct_num"),
      opt("az_sos_committee_id"),
      opt("wa_pdc_filer_id"),
      opt("me_ethics_org_id")))
}
