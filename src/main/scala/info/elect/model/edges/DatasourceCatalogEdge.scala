// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model.edges

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}
import info.elect.model.SchemaBase

/** (CatalogMeta)-[:HAS_CATALOG]->(CatalogMeta) */
object DatasourceCatalogEdge extends SchemaBase {

  val tableName = "datasource_catalog_edges"
  val relType = "HAS_CATALOG"
  val srcLabel = "CatalogMeta"
  val dstLabel = "CatalogMeta"

  val schema: StructType = StructType(edgeBase)
}
