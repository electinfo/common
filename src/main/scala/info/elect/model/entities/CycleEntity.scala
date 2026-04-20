// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, DateType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Election cycles (2-year periods) */
object CycleEntity extends SchemaBase {

  val tableName = "cycle_entities"
  val label = "Cycle"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("cycle_year", LongType),
      opt("start_date", DateType),
      opt("end_date", DateType),
      opt("cycle_type")))
}
