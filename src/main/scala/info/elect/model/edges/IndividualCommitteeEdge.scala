// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, DateType, DoubleType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Individual)-[:CONTRIBUTED_TO]->(Committee) */
object IndividualCommitteeEdge extends SchemaBase {

  val tableName = "individual_committee_edges"
  val relType = "CONTRIBUTED_TO"
  val srcLabel = "Individual"
  val dstLabel = "Committee"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("total_amount", DoubleType),
      opt("contribution_count", LongType),
      opt("first_contribution", DateType),
      opt("last_contribution", DateType),
      opt("transaction_types"),
      opt("cycles")))
}
