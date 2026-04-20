// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Political offices (seats) */
object OfficeEntity extends SchemaBase {

  val tableName = "office_entities"
  val label = "Office"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("office_key"),
      req("office_type"),
      opt("state"),
      opt("district"),
      opt("chamber")))
}
