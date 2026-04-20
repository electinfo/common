// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, DateType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (Individual)-[:EMPLOYED_BY]->(Employer) */
object IndividualEmployerEdge extends SchemaBase {

  val tableName = "individual_employer_edges"
  val relType = "EMPLOYED_BY"
  val srcLabel = "Individual"
  val dstLabel = "Employer"

  val schema: StructType = StructType(
    edgeBase ++ Seq(
      opt("occupation"),
      opt("record_count", LongType),
      opt("first_seen", DateType),
      opt("last_seen", DateType),
      opt("cycles")))
}
