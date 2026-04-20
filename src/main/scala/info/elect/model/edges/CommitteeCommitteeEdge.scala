// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, DateType, DoubleType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Committee)-[:TRANSFERRED_TO]->(Committee) */
object CommitteeCommitteeEdge extends SchemaBase {

  val tableName = "committee_committee_edges"
  val relType = "TRANSFERRED_TO"
  val srcLabel = "Committee"
  val dstLabel = "Committee"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("total_amount", DoubleType),
      opt("transaction_count", LongType),
      opt("first_transaction", DateType),
      opt("last_transaction", DateType),
      opt("cycles")))
}
