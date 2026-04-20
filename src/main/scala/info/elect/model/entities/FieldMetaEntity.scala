// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{BooleanType, DataType, IntegerType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Meta-entity representing a field across catalogs */
object FieldMetaEntity extends SchemaBase {

  val tableName = "field_meta_entities"
  val label = "FieldMeta"

  val schema: StructType = StructType(
    entityBase ++ Seq(
      req("table_type"),
      req("field_name"),
      opt("data_type"),
      opt("is_required", BooleanType),
      opt("catalog_count", IntegerType),
      opt("catalogs")))
}
