"""
Enterprise-flavored UUID5 helpers.

Thin convenience wrappers around siege_utilities.identifiers that bind
the generic ``uuid5_from_seed`` / ``attestation_uuid`` machinery to the
enterprise namespace constants.

Callers must use these wrappers — never call ``uuid.uuid5`` or
``siege_utilities.identifiers.uuid5_from_seed`` directly outside this
module. The CI lint rule (added in PC-16a) enforces this.

Seed-string conventions:

- person_uuid:   "FEC_CAND:H4VA07136" | "STATE_CAND:TX:E12345" | "VOTERFILE:<id>"
- committee_uuid: "FEC_CMTE:C00401224" | "STATE_CMTE:TX:M12345"
- organization_uuid: "EIN:123456789" | "SEC_CIK:0001234567" | "STATE_CORP:TX:0001234"
- office_uuid:   "<office_code>:<state>:<district>"
- seat_uuid:     "<office_code>:<state>:<district>:<senate_class?>"
- attestation_uuid: see attestation_uuid() docstring

Relocated 2026-05-19 from ``enterprise/uuid_generation.py``. Logic
unchanged — every output for every input is bit-identical to what
ESQ silver translate produces.
"""

from uuid import UUID

from siege_utilities.identifiers import (
    attestation_uuid as _attestation_uuid,
    uuid5_from_seed,
)

from electinfo_common.identifiers.namespaces import (
    ATTESTATION_NS,
    COMMITTEE_NS,
    OFFICE_NS,
    ORGANIZATION_NS,
    PERSON_NS,
    SEAT_NS,
)


def person_uuid(seed: str) -> UUID:
    """Person UUID5 from a canonical seed (ladder per ontology §19.3).

    Seed examples:
        "FEC_CAND:H4VA07136"           — federal candidate (most specific)
        "STATE_CAND:TX:E12345"         — state candidate
        "VOTERFILE:<voterfile_id>"    — voter file match
        "NAME_DOB:<normalized_name>:<dob_yyyymmdd>" — fallback resolution
    """
    return uuid5_from_seed(PERSON_NS, seed)


def committee_uuid(seed: str) -> UUID:
    """Committee UUID5 from FEC_CMTE / STATE_CMTE / composite fallback.

    Seed examples:
        "FEC_CMTE:C00401224"           — ActBlue
        "STATE_CMTE:TX:M12345"
    """
    return uuid5_from_seed(COMMITTEE_NS, seed)


def organization_uuid(seed: str) -> UUID:
    """Organization UUID5 from EIN / SEC_CIK / STATE_CORP / DUNS / NAME_HASH.

    Seed examples:
        "EIN:123456789"
        "SEC_CIK:0001234567"
        "STATE_CORP:TX:0001234"
        "NAME_HASH:<sha256-of-normalized-name>"
    """
    return uuid5_from_seed(ORGANIZATION_NS, seed)


def office_uuid(office_code: str, state_code: str | None, district_label: str) -> UUID:
    """Office UUID5 from composite (office_code, state, district)."""
    state_part = state_code or ""
    seed = f"{office_code}:{state_part}:{district_label}"
    return uuid5_from_seed(OFFICE_NS, seed)


def seat_uuid(
    office_code: str,
    state_code: str | None,
    district_label: str,
    senate_class: int | None = None,
) -> UUID:
    """Seat UUID5. senate_class differentiates Senate seats in the same state."""
    state_part = state_code or ""
    class_part = str(senate_class) if senate_class is not None else ""
    seed = f"{office_code}:{state_part}:{district_label}:{class_part}"
    return uuid5_from_seed(SEAT_NS, seed)


def attestation_uuid(
    source_artifact_hash: str,
    parsed_record_line: int,
    parser_version: str,
    attested_values_hash: str,
) -> UUID:
    """
    Attestation UUID5 including parser_version for idempotent re-parse.

    Thin wrapper around ``siege_utilities.identifiers.attestation_uuid``
    that binds the enterprise ATTESTATION_NS.
    """
    return _attestation_uuid(
        namespace=ATTESTATION_NS,
        source_artifact_hash=source_artifact_hash,
        record_line=parsed_record_line,
        parser_version=parser_version,
        values_hash=attested_values_hash,
    )
