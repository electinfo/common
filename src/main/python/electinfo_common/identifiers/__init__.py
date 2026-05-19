"""electinfo_common.identifiers — frozen UUID5 namespaces + entity-typed wrappers.

This is the **single source of truth** for UUID5 generation across every
electinfo pipeline (ESQ silver translate, EE dlt-hub writer, rundeck
quicksilver transformations, future state-source pipelines).

Rule: no code outside this module should ever call ``uuid.uuid5(`` or
``siege_utilities.identifiers.uuid5_from_seed`` directly. All entity ID
generation imports a typed wrapper (``person_uuid``, ``committee_uuid``,
etc.) from here. A CI lint rule enforces this — see electinfo/rundeck#438
(PC-16a).

The namespace constants are **frozen** by elect.info derivation. Changing
any of them silently invalidates every UUID5 written to the warehouse and
produces duplicate canonical entities. Tests verify each hardcoded
constant matches its ``siege_utilities.identifiers.derive_sub_namespace``
derivation — drift is a fatal build failure.
"""

from electinfo_common.identifiers.namespaces import (
    ALL_NAMESPACES,
    ATTESTATION_NS,
    BALLOT_MEASURE_NS,
    CANDIDACY_NS,
    COMMITTEE_NS,
    CONTRIBUTION_LIMIT_NS,
    ELECTION_CYCLE_NS,
    ELECTION_NS,
    OFFICE_NS,
    ORGANIZATION_NS,
    PERSON_NS,
    ROOT_NAMESPACE,
    ROOT_SEED_INPUT,
    SEAT_NS,
)
from electinfo_common.identifiers.uuid_generation import (
    attestation_uuid,
    committee_uuid,
    office_uuid,
    organization_uuid,
    person_uuid,
    seat_uuid,
)

__all__ = [
    # Namespace constants
    "ROOT_SEED_INPUT",
    "ROOT_NAMESPACE",
    "PERSON_NS",
    "COMMITTEE_NS",
    "ORGANIZATION_NS",
    "OFFICE_NS",
    "SEAT_NS",
    "CANDIDACY_NS",
    "ATTESTATION_NS",
    "CONTRIBUTION_LIMIT_NS",
    "ELECTION_NS",
    "ELECTION_CYCLE_NS",
    "BALLOT_MEASURE_NS",
    "ALL_NAMESPACES",
    # Typed wrappers
    "person_uuid",
    "committee_uuid",
    "organization_uuid",
    "office_uuid",
    "seat_uuid",
    "attestation_uuid",
]
