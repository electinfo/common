import pytest

from electinfo_common import canonical_path


@pytest.mark.parametrize(
    "entity_type, entity_id, expected",
    [
        ("Candidate", "P80000722", "candidates/p80000722"),
        ("Candidate", "H6CA12345", "candidates/h6ca12345"),
        ("Committee", "C00401224", "committees/c00401224"),
        ("Individual", "I-a7f3b2c1e9d8f4a6", "individuals/i-a7f3b2c1e9d8f4a6"),
        ("Employer", "O-8b3f1a2e9c7d5b4a", "employers/o-8b3f1a2e9c7d5b4a"),
        ("Vendor", "V-4c2e8a1f3b7d6e9c", "vendors/v-4c2e8a1f3b7d6e9c"),
        ("Party", "DEM", "parties/dem"),
        ("State", "CA", "states/ca"),
        ("District", "CA-12", "districts/ca-12"),
        ("Office", "S-CA", "offices/s-ca"),
        ("Cycle", "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "cycles/a1b2c3d4-e5f6-7890-abcd-ef1234567890"),
        ("County", "06037", "counties/06037"),
        ("Place", "0644000", "places/0644000"),
        ("PostalCode", "90210", "postalcodes/90210"),
        ("Precinct", "A1B2C3D4-E5F6-7890-ABCD-EF1234567890", "precincts/a1b2c3d4-e5f6-7890-abcd-ef1234567890"),
    ],
)
def test_canonical_path(entity_type, entity_id, expected):
    assert canonical_path(entity_type, entity_id) == expected


def test_canonical_path_lowercases_id():
    assert canonical_path("State", "TX") == "states/tx"


def test_canonical_path_unknown_type():
    with pytest.raises(ValueError, match="Unknown entity type"):
        canonical_path("Unknown", "123")
