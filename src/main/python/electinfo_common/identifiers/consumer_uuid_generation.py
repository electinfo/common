"""
Consumer-side UUID5 wrappers (Neo4j / API / static HTML ontology).

Each wrapper binds a Consumer entity-type namespace from
``consumer_namespaces`` and the generic ``siege_utilities.identifiers``
machinery. Use these from rundeck-quicksilver pipelines and any Consumer-
target writer.

Naming convention: ``consumer_<lowercase_type>_uuid``. The ``consumer_``
prefix prevents confusion with the Enterprise-ontology wrappers
(``person_uuid``, ``committee_uuid``, etc.) which target a different
ontology entirely.

Seed convention: the second argument is a raw source-system identifier
(e.g. an FEC committee ID like ``"C00401224"``, a normalized name hash,
a state-prefixed code like ``"MNCFB-1234"``). The library does NOT
downcase or normalize — callers control the canonical form.

See ``project_enterprise_vs_consumer_ontology`` in workspace memory for
the two-ontology picture and entity-types.json for the canonical
CamelCase labels.
"""

from uuid import UUID

from siege_utilities.identifiers import uuid5_from_seed

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
)


def consumer_politician_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Politician (candidates, elected officials).

    Seed examples:
        "FEC_CAND:H4VA07136"
        "STATE_CAND:TX:E12345"
    """
    return uuid5_from_seed(CONSUMER_POLITICIAN_NS, seed)


def consumer_candidate_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Candidate. Same seed conventions as Politician.

    Note: Consumer distinguishes Politician (the persistent person) from
    Candidate (a specific candidacy/race-cycle binding). Don't conflate.
    """
    return uuid5_from_seed(CONSUMER_CANDIDATE_NS, seed)


def consumer_committee_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Committee.

    Seed examples:
        "C00401224"              — bare FEC committee ID (rundeck legacy convention)
        "MNCFB-12345"            — state-prefixed
        "VADOE-67890"
    """
    return uuid5_from_seed(CONSUMER_COMMITTEE_NS, seed)


def consumer_individual_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Individual (donor identity in the consumer graph).

    Seed examples:
        "NAME_HASH:<sha256-of-normalized-name-city-state-zip>"
    """
    return uuid5_from_seed(CONSUMER_INDIVIDUAL_NS, seed)


def consumer_employer_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Employer (organization-as-employer role)."""
    return uuid5_from_seed(CONSUMER_EMPLOYER_NS, seed)


def consumer_vendor_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Vendor (organization-as-vendor role)."""
    return uuid5_from_seed(CONSUMER_VENDOR_NS, seed)


def consumer_party_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Party (DEM, REP, IND, etc.)."""
    return uuid5_from_seed(CONSUMER_PARTY_NS, seed)


def consumer_state_uuid(state_fips: str) -> UUID:
    """UUID5 for a Consumer State, keyed on 2-digit FIPS."""
    return uuid5_from_seed(CONSUMER_STATE_NS, state_fips)


def consumer_district_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer District (CD / SLDL / SLDU)."""
    return uuid5_from_seed(CONSUMER_DISTRICT_NS, seed)


def consumer_office_uuid(office_type: str, state: str | None, district: str) -> UUID:
    """UUID5 for a Consumer Office.

    Seed: ``"<office_type>|<state>|<district>"``. Matches rundeck's
    UUID5_SQL('Office', 'office_type', 'state', 'district') composite.
    """
    state_part = state or ""
    seed = f"{office_type}|{state_part}|{district}"
    return uuid5_from_seed(CONSUMER_OFFICE_NS, seed)


def consumer_race_uuid(
    state: str, election_year: str, office_type: str, district: str | None
) -> UUID:
    """UUID5 for a Consumer Race.

    Seed: ``"<state>|<election_year>|<office_type>|<district>"``. Matches
    rundeck's UUID5_SQL('Race', 'state', 'election_year_str', 'office_type',
    "COALESCE(district, '')").
    """
    district_part = district or ""
    seed = f"{state}|{election_year}|{office_type}|{district_part}"
    return uuid5_from_seed(CONSUMER_RACE_NS, seed)


def consumer_cycle_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Cycle (election cycle year, e.g. ``"2024"``)."""
    return uuid5_from_seed(CONSUMER_CYCLE_NS, seed)


def consumer_data_source_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer DataSource (FEC, MNCFB, VADOE, RDH, etc.)."""
    return uuid5_from_seed(CONSUMER_DATA_SOURCE_NS, seed)


def consumer_county_uuid(geoid: str) -> UUID:
    """UUID5 for a Consumer County, keyed on 5-digit GEOID (state+county FIPS)."""
    return uuid5_from_seed(CONSUMER_COUNTY_NS, geoid)


def consumer_place_uuid(geoid: str) -> UUID:
    """UUID5 for a Consumer Place (city/town), keyed on 7-digit GEOID."""
    return uuid5_from_seed(CONSUMER_PLACE_NS, geoid)


def consumer_postal_code_uuid(zcta5: str) -> UUID:
    """UUID5 for a Consumer PostalCode (ZCTA5)."""
    return uuid5_from_seed(CONSUMER_POSTAL_CODE_NS, zcta5)


def consumer_precinct_uuid(seed: str) -> UUID:
    """UUID5 for a Consumer Precinct.

    Seed convention: state-prefixed RDH precinct ID (e.g., ``"RDH:VA:51001-A1"``).
    """
    return uuid5_from_seed(CONSUMER_PRECINCT_NS, seed)


def consumer_tract_uuid(geoid: str) -> UUID:
    """UUID5 for a Consumer Tract, keyed on 11-digit GEOID."""
    return uuid5_from_seed(CONSUMER_TRACT_NS, geoid)


def consumer_block_uuid(geoid: str) -> UUID:
    """UUID5 for a Consumer Block, keyed on 15-digit GEOID."""
    return uuid5_from_seed(CONSUMER_BLOCK_NS, geoid)
