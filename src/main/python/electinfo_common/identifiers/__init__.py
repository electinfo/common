"""electinfo_common.identifiers — frozen UUID5 namespaces + entity-typed wrappers.

This is the **single source of truth** for UUID5 generation across every
electinfo pipeline (ESQ silver translate, EE dlt-hub writer, rundeck
quicksilver transformations, future state-source pipelines).

**TWO ontologies.** Enterprise and Consumer have intentionally different
entity-type vocabularies (see ``project_enterprise_vs_consumer_ontology``
in workspace memory):

- **Enterprise** (PSQL warehouse, source of truth) — lowercase seeds:
  ``Person``, ``Committee``, ``Organization``, ``Office``, ``Seat``,
  ``Candidacy``, ``Election``, ``BallotMeasure``, ``Attestation``,
  ``ContributionLimit``. Production-locked.
- **Consumer** (Neo4j / API / static HTML) — CamelCase seeds matching
  ``entity-types.json``: ``Politician``, ``Candidate``, ``Committee``,
  ``Individual``, ``Employer``, ``Vendor``, ``Party``, ``State``,
  ``District``, ``Office``, ``Race``, ``Cycle``, ``DataSource``,
  ``County``, ``Place``, ``PostalCode``, ``Precinct``, ``Tract``, ``Block``.

A ``Committee`` exists in BOTH ontologies but with DIFFERENT UUIDs
(``COMMITTEE_NS`` vs ``CONSUMER_COMMITTEE_NS``) because they're different
ontological objects. Tributary projects between them.

Rule: no code outside this module should ever call ``uuid.uuid5(`` or
``siege_utilities.identifiers.uuid5_from_seed`` directly. All entity ID
generation imports a typed wrapper from here.

The namespace constants are **frozen** by elect.info derivation. Changing
any of them silently invalidates every UUID5 written to the warehouse.
Tests verify each hardcoded constant matches its derivation — drift is a
fatal build failure.
"""

# --- Enterprise ontology (PSQL warehouse) ---------------------------------

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

# --- Consumer ontology (Neo4j / API / static HTML) ------------------------

from electinfo_common.identifiers.consumer_namespaces import (
    CONSUMER_BLOCK_NS,
    CONSUMER_CANDIDATE_NS,
    CONSUMER_COMMITTEE_NS,
    CONSUMER_COUNTY_NS,
    CONSUMER_CYCLE_NS,
    CONSUMER_DATA_SOURCE_NS,
    CONSUMER_DISTRICT_NS,
    CONSUMER_EMPLOYER_NS,
    CONSUMER_INDIVIDUAL_NS,
    CONSUMER_NAMESPACES,
    CONSUMER_OFFICE_NS,
    CONSUMER_PARTY_NS,
    CONSUMER_PLACE_NS,
    CONSUMER_POLITICIAN_NS,
    CONSUMER_POSTAL_CODE_NS,
    CONSUMER_PRECINCT_NS,
    CONSUMER_RACE_NS,
    CONSUMER_STATE_NS,
    CONSUMER_TRACT_NS,
    CONSUMER_VENDOR_NS,
    get_consumer_namespace,
)
from electinfo_common.identifiers.consumer_uuid_generation import (
    consumer_block_uuid,
    consumer_candidate_uuid,
    consumer_committee_uuid,
    consumer_county_uuid,
    consumer_cycle_uuid,
    consumer_data_source_uuid,
    consumer_district_uuid,
    consumer_employer_uuid,
    consumer_individual_uuid,
    consumer_office_uuid,
    consumer_party_uuid,
    consumer_place_uuid,
    consumer_politician_uuid,
    consumer_postal_code_uuid,
    consumer_precinct_uuid,
    consumer_race_uuid,
    consumer_state_uuid,
    consumer_tract_uuid,
    consumer_vendor_uuid,
)

__all__ = [
    # Shared
    "ROOT_SEED_INPUT",
    "ROOT_NAMESPACE",
    # Enterprise namespace constants
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
    # Enterprise wrappers
    "person_uuid",
    "committee_uuid",
    "organization_uuid",
    "office_uuid",
    "seat_uuid",
    "attestation_uuid",
    # Consumer namespace constants
    "CONSUMER_POLITICIAN_NS",
    "CONSUMER_CANDIDATE_NS",
    "CONSUMER_COMMITTEE_NS",
    "CONSUMER_INDIVIDUAL_NS",
    "CONSUMER_EMPLOYER_NS",
    "CONSUMER_VENDOR_NS",
    "CONSUMER_PARTY_NS",
    "CONSUMER_STATE_NS",
    "CONSUMER_DISTRICT_NS",
    "CONSUMER_OFFICE_NS",
    "CONSUMER_RACE_NS",
    "CONSUMER_CYCLE_NS",
    "CONSUMER_DATA_SOURCE_NS",
    "CONSUMER_COUNTY_NS",
    "CONSUMER_PLACE_NS",
    "CONSUMER_POSTAL_CODE_NS",
    "CONSUMER_PRECINCT_NS",
    "CONSUMER_TRACT_NS",
    "CONSUMER_BLOCK_NS",
    "CONSUMER_NAMESPACES",
    "get_consumer_namespace",
    # Consumer wrappers
    "consumer_politician_uuid",
    "consumer_candidate_uuid",
    "consumer_committee_uuid",
    "consumer_individual_uuid",
    "consumer_employer_uuid",
    "consumer_vendor_uuid",
    "consumer_party_uuid",
    "consumer_state_uuid",
    "consumer_district_uuid",
    "consumer_office_uuid",
    "consumer_race_uuid",
    "consumer_cycle_uuid",
    "consumer_data_source_uuid",
    "consumer_county_uuid",
    "consumer_place_uuid",
    "consumer_postal_code_uuid",
    "consumer_precinct_uuid",
    "consumer_tract_uuid",
    "consumer_block_uuid",
]
