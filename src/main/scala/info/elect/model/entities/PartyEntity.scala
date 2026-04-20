// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Political parties */
object PartyEntity extends SchemaBase {

  val tableName = "party_entities"
  val label = "Party"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("party_code"),
      opt("party_name"),
      opt("candidate_count", LongType),
      opt("committee_count", LongType),
      opt("active_cycles")))
}
