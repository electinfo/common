"""Verify Consumer namespace constants match their derivations.

If any test here fails, someone has changed a Consumer namespace constant
without updating its CamelCase derivation seed. Every UUID5 derived from
the changed namespace becomes wrong.

The CamelCase entity-type labels come from electinfo_common/schemas/
entity-types.json — single source of truth shared with TypeScript.
"""

from uuid import NAMESPACE_URL, uuid5

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
from electinfo_common.identifiers.namespaces import ROOT_NAMESPACE


def _derive(name: str):
    """Reproduce the derivation chain for one Consumer namespace."""
    return uuid5(ROOT_NAMESPACE, name)


def test_root_namespace_unchanged():
    """Root is shared with Enterprise namespaces; never derives from anything else."""
    assert ROOT_NAMESPACE == uuid5(NAMESPACE_URL, "elect.info")


def test_politician_ns():
    assert CONSUMER_POLITICIAN_NS == _derive("Politician")


def test_candidate_ns():
    assert CONSUMER_CANDIDATE_NS == _derive("Candidate")


def test_committee_ns():
    assert CONSUMER_COMMITTEE_NS == _derive("Committee")


def test_individual_ns():
    assert CONSUMER_INDIVIDUAL_NS == _derive("Individual")


def test_employer_ns():
    assert CONSUMER_EMPLOYER_NS == _derive("Employer")


def test_vendor_ns():
    assert CONSUMER_VENDOR_NS == _derive("Vendor")


def test_party_ns():
    assert CONSUMER_PARTY_NS == _derive("Party")


def test_state_ns():
    assert CONSUMER_STATE_NS == _derive("State")


def test_district_ns():
    assert CONSUMER_DISTRICT_NS == _derive("District")


def test_office_ns():
    assert CONSUMER_OFFICE_NS == _derive("Office")


def test_race_ns():
    assert CONSUMER_RACE_NS == _derive("Race")


def test_cycle_ns():
    assert CONSUMER_CYCLE_NS == _derive("Cycle")


def test_data_source_ns():
    assert CONSUMER_DATA_SOURCE_NS == _derive("DataSource")


def test_county_ns():
    assert CONSUMER_COUNTY_NS == _derive("County")


def test_place_ns():
    assert CONSUMER_PLACE_NS == _derive("Place")


def test_postal_code_ns():
    assert CONSUMER_POSTAL_CODE_NS == _derive("PostalCode")


def test_precinct_ns():
    assert CONSUMER_PRECINCT_NS == _derive("Precinct")


def test_tract_ns():
    assert CONSUMER_TRACT_NS == _derive("Tract")


def test_block_ns():
    assert CONSUMER_BLOCK_NS == _derive("Block")


def test_camelcase_strict_lookup():
    """get_consumer_namespace is strict CamelCase. 'committee' should NOT match."""
    assert get_consumer_namespace("Committee") == CONSUMER_COMMITTEE_NS
    try:
        get_consumer_namespace("committee")
    except ValueError:
        pass
    else:
        raise AssertionError(
            "get_consumer_namespace should reject lowercase entity-type strings — "
            "the lowercase convention is Enterprise's, not Consumer's"
        )


def test_consumer_namespaces_dict_matches_constants():
    """The CONSUMER_NAMESPACES dict must agree with the individual constants."""
    assert CONSUMER_NAMESPACES["Politician"] == CONSUMER_POLITICIAN_NS
    assert CONSUMER_NAMESPACES["Committee"] == CONSUMER_COMMITTEE_NS
    assert CONSUMER_NAMESPACES["Block"] == CONSUMER_BLOCK_NS


def test_consumer_namespaces_distinct_from_enterprise():
    """Consumer 'Committee' UUID must differ from Enterprise 'committee' UUID.

    Same root, different sub-namespace seeds (CamelCase vs lowercase) →
    different namespaces. If these EVER collide, something is wrong.
    """
    from electinfo_common.identifiers.namespaces import COMMITTEE_NS as ENTERPRISE_COMMITTEE_NS

    assert CONSUMER_COMMITTEE_NS != ENTERPRISE_COMMITTEE_NS


def test_consumer_namespaces_all_distinct():
    """Every Consumer namespace must differ from every other."""
    constants = list(CONSUMER_NAMESPACES.values())
    assert len(set(constants)) == len(constants)
