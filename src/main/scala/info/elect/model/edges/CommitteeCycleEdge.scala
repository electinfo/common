// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Committee)-[:ACTIVE_IN_CYCLE]->(Cycle) */
object CommitteeCycleEdge extends SchemaBase {

  val tableName = "committee_cycle_edges"
  val relType = "ACTIVE_IN_CYCLE"
  val srcLabel = "Committee"
  val dstLabel = "Cycle"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("fec_committee_id"),
      opt("cycle_year", IntegerType),
      opt("committee_type"),
      opt("committee_designation"),
      opt("party_affiliation"),
      opt("filing_frequency"),
      opt("organization_type"),
      opt("linked_candidate_id")))
}
