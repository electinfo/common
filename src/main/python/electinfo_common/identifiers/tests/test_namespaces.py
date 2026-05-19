"""Tests that the hardcoded namespace constants match their derivations.

If any test here fails, someone has changed a namespace constant without
also updating its derivation seed. That's a fatal data-integrity bug —
every UUID5 derived from the changed namespace becomes wrong.
"""

from siege_utilities.identifiers import derive_root, derive_sub_namespace

from electinfo_common.identifiers.namespaces import (
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


def test_root_namespace_matches_derivation():
    assert ROOT_NAMESPACE == derive_root(ROOT_SEED_INPUT)


def test_person_ns_derivation():
    assert PERSON_NS == derive_sub_namespace(ROOT_NAMESPACE, "person")


def test_committee_ns_derivation():
    assert COMMITTEE_NS == derive_sub_namespace(ROOT_NAMESPACE, "committee")


def test_organization_ns_derivation():
    assert ORGANIZATION_NS == derive_sub_namespace(ROOT_NAMESPACE, "organization")


def test_office_ns_derivation():
    assert OFFICE_NS == derive_sub_namespace(ROOT_NAMESPACE, "office")


def test_seat_ns_derivation():
    assert SEAT_NS == derive_sub_namespace(ROOT_NAMESPACE, "seat")


def test_candidacy_ns_derivation():
    assert CANDIDACY_NS == derive_sub_namespace(ROOT_NAMESPACE, "candidacy")


def test_attestation_ns_derivation():
    assert ATTESTATION_NS == derive_sub_namespace(ROOT_NAMESPACE, "attestation")


def test_contribution_limit_ns_derivation():
    assert CONTRIBUTION_LIMIT_NS == derive_sub_namespace(
        ROOT_NAMESPACE, "contribution_limit"
    )


def test_election_ns_derivation():
    assert ELECTION_NS == derive_sub_namespace(ROOT_NAMESPACE, "election")


def test_election_cycle_ns_derivation():
    assert ELECTION_CYCLE_NS == derive_sub_namespace(ROOT_NAMESPACE, "election_cycle")


def test_ballot_measure_ns_derivation():
    assert BALLOT_MEASURE_NS == derive_sub_namespace(ROOT_NAMESPACE, "ballot_measure")


def test_namespaces_are_distinct():
    """Sanity: every namespace constant differs from every other."""
    constants = [
        ROOT_NAMESPACE,
        PERSON_NS,
        COMMITTEE_NS,
        ORGANIZATION_NS,
        OFFICE_NS,
        SEAT_NS,
        CANDIDACY_NS,
        ATTESTATION_NS,
        CONTRIBUTION_LIMIT_NS,
        ELECTION_NS,
        ELECTION_CYCLE_NS,
        BALLOT_MEASURE_NS,
    ]
    assert len(set(constants)) == len(constants)
