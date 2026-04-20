// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Elected officials (congress.gov sourced) */
object OfficeholderEntity extends SchemaBase {

  val tableName = "officeholder_entities"
  val label = "Officeholder"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      opt("bioguide_id"),
      req("name"),
      opt("first_name"),
      opt("last_name"),
      opt("birth_year"),
      opt("death_year"),
      opt("is_current"),
      opt("most_recent_state"),
      opt("most_recent_party"),
      opt("most_recent_chamber"),
      opt("portrait_url")))
}
