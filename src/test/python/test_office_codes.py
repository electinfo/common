from electinfo_common import office_codes


def test_federal_offices():
    assert "P" in office_codes.federal
    assert "S" in office_codes.federal
    assert "H" in office_codes.federal
    assert len(office_codes.federal) == 3


def test_state_executive_offices():
    assert "GOV" in office_codes.state_executive
    assert "LTGOV" in office_codes.state_executive
    assert "AG" in office_codes.state_executive
    assert "SOS" in office_codes.state_executive
    assert "TREAS" in office_codes.state_executive


def test_state_legislative_offices():
    assert "SS" in office_codes.state_legislative
    assert "SR" in office_codes.state_legislative
    assert len(office_codes.state_legislative) == 2


def test_codes_is_flat_union():
    total = (
        len(office_codes.federal)
        + len(office_codes.state_executive)
        + len(office_codes.state_legislative)
        + len(office_codes.local)
    )
    assert len(office_codes.codes) == total


def test_names_lookup():
    assert office_codes.names["P"] == "President of the United States"
    assert office_codes.names["S"] == "U.S. Senator"
    assert office_codes.names["GOV"] == "Governor"
    assert office_codes.names["SS"] == "State Senator"
    assert office_codes.names["SR"] == "State Representative"


def test_normalize_canonical_code():
    assert office_codes.normalize("P") == "P"
    assert office_codes.normalize("GOV") == "GOV"
    assert office_codes.normalize("SS") == "SS"


def test_normalize_full_name():
    assert office_codes.normalize("Governor") == "GOV"
    assert office_codes.normalize("State Senator") == "SS"
    assert office_codes.normalize("State Representative") == "SR"
    assert office_codes.normalize("Attorney General") == "AG"


def test_normalize_pa_dos_abbreviations():
    assert office_codes.normalize("LTG") == "LTGOV"
    assert office_codes.normalize("ATT") == "AG"
    assert office_codes.normalize("TRS") == "TREAS"
    assert office_codes.normalize("STH") == "SR"
    assert office_codes.normalize("STS") == "SS"


def test_normalize_openelections_alias():
    assert office_codes.normalize("SH") == "SR"


def test_normalize_federal_full_names():
    assert office_codes.normalize("President") == "P"
    assert office_codes.normalize("U.S. Senator") == "S"
    assert office_codes.normalize("U.S. Representative") == "H"
    assert office_codes.normalize("Representative in Congress") == "H"


def test_normalize_case_insensitive():
    assert office_codes.normalize("governor") == "GOV"
    assert office_codes.normalize("GOVERNOR") == "GOV"
    assert office_codes.normalize("state senator") == "SS"


def test_normalize_unknown_returns_none():
    assert office_codes.normalize("DOGCATCHER") is None


def test_normalize_empty_returns_none():
    assert office_codes.normalize("") is None
    assert office_codes.normalize(None) is None
