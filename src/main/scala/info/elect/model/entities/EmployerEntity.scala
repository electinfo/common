// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DateType, DoubleType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Employers of individual donors */
object EmployerEntity extends SchemaBase {

  val tableName = "employer_entities"
  val label = "Employer"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("name_normalized"),
      opt("employee_donor_count", LongType),
      opt("total_employee_contributions", DoubleType),
      opt("contribution_count", LongType),
      opt("committee_count", IntegerType),
      opt("first_contribution", DateType),
      opt("last_contribution", DateType),
      opt("cycles")))
}
