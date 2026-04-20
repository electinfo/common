// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model

import org.apache.spark.sql.types.{DataType, StringType, StructField, StructType}

/**
 * Shared helpers and base column sequences for quicksilver schemas.
 * Entity and edge objects extend this to inherit req/opt builders and base columns.
 */
trait SchemaBase {

  val ORIGIN_CATALOG = "catalog"

  /** Required column -- source must provide this. */
  protected def req(name: String, dt: DataType = StringType): StructField =
    StructField(name, dt, nullable = false)

  /** Optional column -- null-filled if source doesn't have it. */
  protected def opt(name: String, dt: DataType = StringType): StructField =
    StructField(name, dt, nullable = true)

  protected val entityBase: Seq[StructField] = Seq(opt(ORIGIN_CATALOG), req("id"), req("type"))

  protected val edgeBase: Seq[StructField] = Seq(opt(ORIGIN_CATALOG), req("src"), req("dst"), req("src_type"), req("dst_type"), req("relationship"))
}

object SchemaBase extends SchemaBase
