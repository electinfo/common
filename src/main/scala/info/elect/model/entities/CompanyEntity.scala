// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Corporate entities (LEI-identified) */
object CompanyEntity extends SchemaBase {

  val tableName = "company_entities"
  val label = "Company"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("name"),
      opt("name_normalized"),
      opt("lei"),
      opt("city"),
      opt("state"),
      opt("entity_category"),
      opt("entity_status"),
      opt("legal_form_code"),
      opt("jurisdiction_country"),
      opt("jurisdiction_subdivision")))
}
