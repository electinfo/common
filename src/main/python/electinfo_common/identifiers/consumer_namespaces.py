"""
Consumer UUID5 namespace constants (Neo4j / API / static HTML ontology).

The Consumer ontology is **separate from and intentionally different from**
the Enterprise ontology in ``electinfo_common.identifiers.namespaces``. See
``project_enterprise_vs_consumer_ontology`` in workspace memory for the
full picture.

Source of truth for the entity-type names is ``electinfo_common/schemas/
entity-types.json``. Every Consumer namespace constant in this module is
derived from one of the 19 canonical types in that file, using the
**CamelCase** label exactly as it appears in Neo4j node labels and the
TypeScript / Python entity-type registry.

Why CamelCase here (vs lowercase in ``namespaces.py``):

- The Consumer ontology uses CamelCase by convention (Neo4j labels,
  TypeScript types, JSON schema keys). The namespace seeds match that
  convention so the derivation is transparent.
- The Enterprise namespaces use lowercase seeds (``"person"``, ``"committee"``,
  etc.) because that was the original convention when the Enterprise
  warehouse was built. Those constants are production-locked.

Both ontologies share the same ROOT_NAMESPACE (derived from ``"elect.info"``).
A ``"Committee"`` in the Consumer ontology and a ``"committee"`` in the
Enterprise ontology produce **different** sub-namespaces (and thus different
UUIDs for the same source ID) — that's correct because they're different
ontological objects.

Never change an existing constant value. Add new ones additively. Tests
verify each constant matches its derivation.
"""

from uuid import UUID

# Re-import ROOT from the Enterprise namespaces so it's a single shared
# value (both ontologies hang off the same elect.info root).
from electinfo_common.identifiers.namespaces import ROOT_NAMESPACE

# --- 19 Consumer entity-type namespace constants ---------------------------
# Each derived from the CamelCase canonical type in entity-types.json.
# Test verifies: CONSUMER_<TYPE>_NS == uuid5(ROOT_NAMESPACE, "<CamelCaseType>")

CONSUMER_POLITICIAN_NS = UUID("8b9dc8e7-00fc-5f76-b5ec-b3c72d0a0ad4")
CONSUMER_CANDIDATE_NS = UUID("0826514f-a057-55d2-b4db-34eca22e330f")
CONSUMER_COMMITTEE_NS = UUID("0a421184-5fb7-5b65-bb79-24b6f6171adb")
CONSUMER_INDIVIDUAL_NS = UUID("ea54fe4a-7450-5f73-92c8-64cf2690fc9a")
CONSUMER_EMPLOYER_NS = UUID("912b84d5-3c09-5b3d-9d9d-d37cd1fd3cf1")
CONSUMER_VENDOR_NS = UUID("201c0064-cd83-5f5a-8f36-9de513c8dbae")
CONSUMER_PARTY_NS = UUID("746605a6-c62e-5376-8cd9-6e0222af3cc1")
CONSUMER_STATE_NS = UUID("7f20d5cf-e841-5a78-8308-d61688281c12")
CONSUMER_DISTRICT_NS = UUID("820e8aa9-1b5a-5fdf-a184-8c303d241ead")
CONSUMER_OFFICE_NS = UUID("55fe8445-c219-553b-bf09-6d3d044cf7f2")
CONSUMER_RACE_NS = UUID("a597c48b-ef0c-5011-9978-244f93706590")
CONSUMER_CYCLE_NS = UUID("3a36097d-ba49-5a15-9c84-9f0e0e9f1e79")
CONSUMER_DATA_SOURCE_NS = UUID("5d2787c9-82f7-571a-8232-06008c01423b")
CONSUMER_COUNTY_NS = UUID("446ca402-6748-5f71-8f56-7b9e1590fe0d")
CONSUMER_PLACE_NS = UUID("13324320-8073-5de1-8f10-665d742523d6")
CONSUMER_POSTAL_CODE_NS = UUID("35cad127-9c8f-58b0-93cd-0a6a2bcabc5c")
CONSUMER_PRECINCT_NS = UUID("0898dd5c-09f1-5f48-a020-4b8db8e11aeb")
CONSUMER_TRACT_NS = UUID("29d87d2d-fc7b-5d0f-82ff-e3ce0dc0d173")
CONSUMER_BLOCK_NS = UUID("c7b34982-1f80-5bb5-a9cb-25e602a7b1fd")


# --- CamelCase entity-type label → namespace UUID lookup -------------------
# Used by the typed wrappers and by Spark UDF dispatch. The keys match
# entity-types.json EXACTLY (CamelCase) so any code that asks for the
# canonical type by its Neo4j label finds the right namespace.

CONSUMER_NAMESPACES: dict[str, UUID] = {
    "Politician": CONSUMER_POLITICIAN_NS,
    "Candidate": CONSUMER_CANDIDATE_NS,
    "Committee": CONSUMER_COMMITTEE_NS,
    "Individual": CONSUMER_INDIVIDUAL_NS,
    "Employer": CONSUMER_EMPLOYER_NS,
    "Vendor": CONSUMER_VENDOR_NS,
    "Party": CONSUMER_PARTY_NS,
    "State": CONSUMER_STATE_NS,
    "District": CONSUMER_DISTRICT_NS,
    "Office": CONSUMER_OFFICE_NS,
    "Race": CONSUMER_RACE_NS,
    "Cycle": CONSUMER_CYCLE_NS,
    "DataSource": CONSUMER_DATA_SOURCE_NS,
    "County": CONSUMER_COUNTY_NS,
    "Place": CONSUMER_PLACE_NS,
    "PostalCode": CONSUMER_POSTAL_CODE_NS,
    "Precinct": CONSUMER_PRECINCT_NS,
    "Tract": CONSUMER_TRACT_NS,
    "Block": CONSUMER_BLOCK_NS,
}


def get_consumer_namespace(entity_type: str) -> UUID:
    """Return the Consumer namespace UUID for a CamelCase entity-type label.

    The lookup is case-strict — ``"Committee"`` works, ``"committee"`` does NOT
    (that's the Enterprise convention; use
    ``electinfo_common.identifiers.namespaces.COMMITTEE_NS`` instead).

    Raises:
        ValueError: if ``entity_type`` is not in CONSUMER_NAMESPACES.
    """
    ns = CONSUMER_NAMESPACES.get(entity_type)
    if ns is None:
        canonical = ", ".join(sorted(CONSUMER_NAMESPACES.keys()))
        raise ValueError(
            f"Unknown Consumer entity type: {entity_type!r}. "
            f"Canonical types (CamelCase, per entity-types.json): {canonical}"
        )
    return ns
