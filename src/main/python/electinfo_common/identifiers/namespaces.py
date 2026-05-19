"""
Enterprise UUID5 namespace constants (elect.info-specific).

Hardcoded values derived from ``elect.info`` via
``siege_utilities.identifiers.derive_root`` and ``derive_sub_namespace``.
Tests verify the hardcoded values match the derivation — any drift is
a fatal build failure.

These constants MUST also match the rows seeded in the ``enterprise_core``
Django migration (``_system_constants`` table). The runtime startup
assertion enforces that invariant.

Never change an existing constant value — doing so would invalidate
every UUID5 derived from it across the warehouse. Additions are
additive: new entity-type namespaces get new constants + new migrated
rows, never altering existing ones.

Relocated 2026-05-19 from ``enterprise/namespaces.py`` to make this
the single shared source across ESQ, EE, rundeck quicksilver, and
future state-source pipelines. The constants themselves are unchanged.
"""

from uuid import UUID

ROOT_SEED_INPUT = "elect.info"

ROOT_NAMESPACE = UUID("2e555641-15f2-578c-ab9b-a0909d1370d0")

PERSON_NS = UUID("f1083706-07fc-55c1-85b7-1ada55f9e814")
COMMITTEE_NS = UUID("513c0235-ec97-51c2-981f-616068c292aa")
ORGANIZATION_NS = UUID("86b4229a-9832-5725-bda3-3bd37cb89057")
OFFICE_NS = UUID("cdedc226-a62c-59e2-91c6-2012ea3db7a1")
SEAT_NS = UUID("18abe7ff-bb66-5d22-b4d6-0e49bedc4916")
CANDIDACY_NS = UUID("9f8fc3aa-b83d-574e-80c6-76ea01a9a9f2")
ATTESTATION_NS = UUID("ca76e869-6f15-5401-b5a0-1088340c8238")
CONTRIBUTION_LIMIT_NS = UUID("2d028a3d-88a8-5e22-8c3e-93c9699ac7cb")
ELECTION_NS = UUID("90a3f8b8-f7be-569a-8442-91ce7f221696")
ELECTION_CYCLE_NS = UUID("60045820-3544-5fb0-a011-d65e990777d2")
BALLOT_MEASURE_NS = UUID("578d9da2-286b-5b18-a49d-e4bdffb3c5e0")

ALL_NAMESPACES: dict[str, UUID] = {
    "root": ROOT_NAMESPACE,
    "person": PERSON_NS,
    "committee": COMMITTEE_NS,
    "organization": ORGANIZATION_NS,
    "office": OFFICE_NS,
    "seat": SEAT_NS,
    "candidacy": CANDIDACY_NS,
    "attestation": ATTESTATION_NS,
    "contribution_limit": CONTRIBUTION_LIMIT_NS,
    "election": ELECTION_NS,
    "election_cycle": ELECTION_CYCLE_NS,
    "ballot_measure": BALLOT_MEASURE_NS,
}
