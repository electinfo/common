// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DateType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Individual donors/contributors */
object IndividualEntity extends SchemaBase {

  val tableName = "individual_entities"
  val label = "Individual"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("first_name"),
      opt("last_name"),
      opt("middle_name"),
      opt("city"),
      opt("state"),
      opt("zip_code"),
      opt("employer"),
      opt("occupation"),
      opt("contribution_count", LongType),
      opt("committee_count", IntegerType),
      opt("first_contribution", DateType),
      opt("last_contribution", DateType),
      opt("cycles")))
}
