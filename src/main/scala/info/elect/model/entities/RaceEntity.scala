// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Electoral races (office + cycle) */
object RaceEntity extends SchemaBase {

  val tableName = "race_entities"
  val label = "Race"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("race_key"),
      opt("office_type"),
      opt("state"),
      opt("district"),
      opt("cycle_year", LongType),
      opt("congress", LongType),
      opt("chamber")))
}
