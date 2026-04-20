// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** US states */
object StateEntity extends SchemaBase {

  val tableName = "state_entities"
  val label = "State"

  val schema: StructType = StructType(entityBase ++ Seq(req("state"), opt("name"), opt("fips")))
}
