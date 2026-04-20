// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DateType, DoubleType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Payees/vendors receiving disbursements from committees */
object VendorEntity extends SchemaBase {

  val tableName = "vendor_entities"
  val label = "Vendor"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("name_normalized"),
      opt("payee_name"),
      opt("payee_normalized"),
      opt("city"),
      opt("state"),
      opt("total_received", DoubleType),
      opt("total_amount", DoubleType),
      opt("payment_count", LongType),
      opt("client_count", IntegerType),
      opt("committee_count", LongType),
      opt("purpose_categories"),
      opt("expn_desc"),
      opt("first_payment", DateType),
      opt("last_payment", DateType),
      opt("cycles")))
}
