// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, DateType, DoubleType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Committee)-[:PAID]->(Vendor) */
object CommitteeVendorEdge extends SchemaBase {

  val tableName = "committee_vendor_edges"
  val relType = "PAID"
  val srcLabel = "Committee"
  val dstLabel = "Vendor"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("total_amount", DoubleType),
      opt("payment_count", LongType),
      opt("purposes"),
      opt("categories"),
      opt("expn_desc"),
      opt("first_payment", DateType),
      opt("last_payment", DateType),
      opt("cycles")))
}
