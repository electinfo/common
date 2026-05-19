"""
Spark UDFs for UUID5 generation — wraps electinfo_common.identifiers wrappers.

For Spark Connect / Spark 4.x with pyarrow available. Uses vectorised
``pandas_udf`` for ~10-100x speedup over row-by-row UDFs at high volume.

Usage in a Spark Connect session:

    from pyspark.sql import functions as F
    from electinfo_common.identifiers.spark_udfs import register_uuid_udfs

    register_uuid_udfs(spark)  # registers all UDFs into the session

    df = spark.read.table("fec_filings.bronze")
    df.withColumn("person_id", F.expr("person_uuid(CONCAT('FEC_CAND:', cand_id))"))
      .withColumn("committee_id", F.expr("committee_uuid(CONCAT('FEC_CMTE:', filer_committee_id))"))

The UDFs accept a single string seed and return a UUID5 as a string.
Callers are responsible for constructing the seed in the canonical
format documented in ``electinfo_common.identifiers.uuid_generation``.

If pyarrow is not available in the executor environment, vectorised
``pandas_udf`` will fall back to row-by-row execution silently — still
correct, just slower. Verify availability with:

    spark.sparkContext.getConf().getAll()
    # Look for spark.sql.execution.arrow.pyspark.enabled
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.sql import SparkSession

from electinfo_common.identifiers.uuid_generation import (
    committee_uuid,
    office_uuid,
    organization_uuid,
    person_uuid,
    seat_uuid,
)


def _make_person_udf():
    """Return a vectorised pandas_udf wrapping ``person_uuid``."""
    import pandas as pd
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql.types import StringType

    @pandas_udf(StringType())
    def _person_uuid_udf(seeds: pd.Series) -> pd.Series:
        return seeds.map(lambda s: str(person_uuid(s)) if s else None)

    return _person_uuid_udf


def _make_committee_udf():
    """Return a vectorised pandas_udf wrapping ``committee_uuid``."""
    import pandas as pd
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql.types import StringType

    @pandas_udf(StringType())
    def _committee_uuid_udf(seeds: pd.Series) -> pd.Series:
        return seeds.map(lambda s: str(committee_uuid(s)) if s else None)

    return _committee_uuid_udf


def _make_organization_udf():
    """Return a vectorised pandas_udf wrapping ``organization_uuid``."""
    import pandas as pd
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql.types import StringType

    @pandas_udf(StringType())
    def _organization_uuid_udf(seeds: pd.Series) -> pd.Series:
        return seeds.map(lambda s: str(organization_uuid(s)) if s else None)

    return _organization_uuid_udf


def _make_office_udf():
    """Return a vectorised pandas_udf wrapping ``office_uuid`` (3-arg)."""
    import pandas as pd
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql.types import StringType

    @pandas_udf(StringType())
    def _office_uuid_udf(
        office_codes: pd.Series, state_codes: pd.Series, district_labels: pd.Series
    ) -> pd.Series:
        return pd.Series(
            [
                str(office_uuid(oc, sc if sc else None, dl or ""))
                if oc is not None
                else None
                for oc, sc, dl in zip(office_codes, state_codes, district_labels)
            ]
        )

    return _office_uuid_udf


def _make_seat_udf():
    """Return a vectorised pandas_udf wrapping ``seat_uuid`` (4-arg)."""
    import pandas as pd
    from pyspark.sql.functions import pandas_udf
    from pyspark.sql.types import StringType

    @pandas_udf(StringType())
    def _seat_uuid_udf(
        office_codes: pd.Series,
        state_codes: pd.Series,
        district_labels: pd.Series,
        senate_classes: pd.Series,
    ) -> pd.Series:
        return pd.Series(
            [
                str(seat_uuid(
                    oc,
                    sc if sc else None,
                    dl or "",
                    int(scl) if scl is not None and scl != "" else None,
                ))
                if oc is not None
                else None
                for oc, sc, dl, scl in zip(office_codes, state_codes, district_labels, senate_classes)
            ]
        )

    return _seat_uuid_udf


def register_uuid_udfs(spark: "SparkSession") -> None:
    """
    Register all UUID5 UDFs into a Spark session.

    After calling this, SQL expressions can use the UDFs by name:

        spark.sql("SELECT person_uuid(CONCAT('FEC_CAND:', cand_id)) AS id FROM ...")

    Idempotent — re-registration overwrites prior definitions.
    """
    spark.udf.register("person_uuid", _make_person_udf())
    spark.udf.register("committee_uuid", _make_committee_udf())
    spark.udf.register("organization_uuid", _make_organization_udf())
    spark.udf.register("office_uuid", _make_office_udf())
    spark.udf.register("seat_uuid", _make_seat_udf())


__all__ = ["register_uuid_udfs"]
