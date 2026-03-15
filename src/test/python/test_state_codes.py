from electinfo_common import state_codes


def test_states_has_50():
    assert len(state_codes.states) == 50


def test_territories_has_6():
    assert len(state_codes.territories) == 6


def test_names_includes_all():
    assert len(state_codes.names) == 57  # 50 states + 6 territories + US


def test_state_name_lookup():
    assert state_codes.names["CA"] == "California"
    assert state_codes.names["TX"] == "Texas"
    assert state_codes.names["DC"] == "District of Columbia"
    assert state_codes.names["US"] == "United States"


def test_fips_to_code():
    assert state_codes.fips_to_code["06"] == "CA"
    assert state_codes.fips_to_code["48"] == "TX"
    assert state_codes.fips_to_code["11"] == "DC"
    assert state_codes.fips_to_code["72"] == "PR"


def test_house_seats():
    assert state_codes.house_seats["CA"] == 52
    assert state_codes.house_seats["TX"] == 38
    assert state_codes.house_seats["WY"] == 1
    assert state_codes.house_seats["DC"] == 0


def test_normalize_code():
    assert state_codes.normalize("CA") == "CA"
    assert state_codes.normalize("TX") == "TX"
    assert state_codes.normalize("DC") == "DC"


def test_normalize_full_name():
    assert state_codes.normalize("California") == "CA"
    assert state_codes.normalize("Texas") == "TX"
    assert state_codes.normalize("District of Columbia") == "DC"


def test_normalize_case_insensitive():
    assert state_codes.normalize("california") == "CA"
    assert state_codes.normalize("TEXAS") == "TX"


def test_normalize_fips():
    assert state_codes.normalize("06") == "CA"
    assert state_codes.normalize("48") == "TX"
    assert state_codes.normalize("6") == "CA"  # handles unpadded


def test_normalize_special():
    assert state_codes.normalize("US") == "US"
    assert state_codes.normalize("United States") == "US"


def test_normalize_unknown_returns_none():
    assert state_codes.normalize("XX") is None
    assert state_codes.normalize("Atlantis") is None


def test_normalize_empty_returns_none():
    assert state_codes.normalize("") is None
    assert state_codes.normalize(None) is None
