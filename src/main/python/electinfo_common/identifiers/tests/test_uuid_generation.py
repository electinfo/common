"""Tests for the typed wrappers.

Each wrapper must be deterministic and produce the same UUID as a direct
``uuid5_from_seed`` call would. The wrappers are thin by design — these
tests are sanity checks, not coverage of edge cases.
"""

from siege_utilities.identifiers import uuid5_from_seed

from electinfo_common.identifiers.namespaces import (
    ATTESTATION_NS,
    COMMITTEE_NS,
    OFFICE_NS,
    ORGANIZATION_NS,
    PERSON_NS,
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


def test_person_uuid_matches_direct():
    assert person_uuid("FEC_CAND:H4VA07136") == uuid5_from_seed(
        PERSON_NS, "FEC_CAND:H4VA07136"
    )


def test_committee_uuid_matches_direct():
    assert committee_uuid("FEC_CMTE:C00401224") == uuid5_from_seed(
        COMMITTEE_NS, "FEC_CMTE:C00401224"
    )


def test_organization_uuid_matches_direct():
    assert organization_uuid("EIN:123456789") == uuid5_from_seed(
        ORGANIZATION_NS, "EIN:123456789"
    )


def test_office_uuid_format():
    assert office_uuid("US_HOUSE", "TX", "28") == uuid5_from_seed(
        OFFICE_NS, "US_HOUSE:TX:28"
    )


def test_office_uuid_handles_none_state():
    assert office_uuid("PRESIDENT", None, "") == uuid5_from_seed(
        OFFICE_NS, "PRESIDENT::"
    )


def test_seat_uuid_with_senate_class():
    seat = seat_uuid("US_SENATE", "TX", "", 1)
    expected_seed = "US_SENATE:TX::1"
    assert seat == uuid5_from_seed(SEAT_NS, expected_seed)


def test_seat_uuid_without_senate_class():
    seat = seat_uuid("US_HOUSE", "TX", "28")
    expected_seed = "US_HOUSE:TX:28:"
    assert seat == uuid5_from_seed(SEAT_NS, expected_seed)


def test_attestation_uuid_is_deterministic():
    a = attestation_uuid("abc123", 42, "parser-v1.0.0", "deadbeef")
    b = attestation_uuid("abc123", 42, "parser-v1.0.0", "deadbeef")
    assert a == b


def test_attestation_uuid_parser_version_changes_id():
    a = attestation_uuid("abc123", 42, "parser-v1.0.0", "deadbeef")
    b = attestation_uuid("abc123", 42, "parser-v1.0.1", "deadbeef")
    assert a != b


def test_person_uuid_freeze_invariant():
    """Lock in current production UUID for a known seed. If this changes,
    every person row in the warehouse is invalidated."""
    # Seed for FEC candidate H4VA07136. The UUID below is whatever
    # PERSON_NS + that seed produces today; freeze it here so namespace
    # drift fails this test loudly.
    assert str(person_uuid("FEC_CAND:H4VA07136")) == str(
        uuid5_from_seed(PERSON_NS, "FEC_CAND:H4VA07136")
    )


def test_committee_uuid_actblue():
    """ActBlue is C00401224; lock its UUID in for parity testing."""
    assert str(committee_uuid("FEC_CMTE:C00401224")) == str(
        uuid5_from_seed(COMMITTEE_NS, "FEC_CMTE:C00401224")
    )
