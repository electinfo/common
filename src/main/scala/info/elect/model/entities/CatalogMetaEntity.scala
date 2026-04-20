// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.entities

import org.apache.spark.sql.types.{DataType, IntegerType, LongType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** Meta-entity representing a Unity Catalog catalog */
object CatalogMetaEntity extends SchemaBase {

  val tableName = "catalog_meta_entities"
  val label = "CatalogMeta"

  val schema: StructType = StructType(entityBase ++ Seq(req("name"), opt("table_count", IntegerType), opt("total_rows", LongType)))
}
