from electinfo_common import party_codes


def test_codes_has_all_fec_parties():
    assert len(party_codes.codes) == 66


def test_canonical_code_lookup():
    assert party_codes.codes["DEM"] == "Democratic Party"
    assert party_codes.codes["REP"] == "Republican Party"
    assert party_codes.codes["GRE"] == "Green Party"
    assert party_codes.codes["IND"] == "Independent"


def test_alias_maps_full_names():
    assert party_codes.aliases["DEMOCRATIC"] == "DEM"
    assert party_codes.aliases["REPUBLICAN"] == "REP"
    assert party_codes.aliases["LIBERTARIAN"] == "LIB"
    assert party_codes.aliases["GREEN"] == "GRE"


def test_alias_maps_single_letters():
    assert party_codes.aliases["D"] == "DEM"
    assert party_codes.aliases["R"] == "REP"
    assert party_codes.aliases["L"] == "LIB"
    assert party_codes.aliases["G"] == "GRE"


def test_alias_maps_full_name_with_party():
    assert party_codes.aliases["DEMOCRATIC PARTY"] == "DEM"
    assert party_codes.aliases["REPUBLICAN PARTY"] == "REP"


def test_alias_maps_nonpartisan_variants():
    assert party_codes.aliases["NO PARTY AFFILIATION"] == "NPA"
    assert party_codes.aliases["NONPARTISAN"] == "NON"
    assert party_codes.aliases["UNAFFILIATED"] == "NPA"


def test_alias_maps_state_specific():
    assert party_codes.aliases["DEMOCRATIC-FARMER-LABOR"] == "DFL"
    assert party_codes.aliases["ALASKAN INDEPENDENCE PARTY"] == "AKI"
    assert party_codes.aliases["LIBERTY UNION"] == "LBU"


def test_normalize_canonical_code():
    assert party_codes.normalize("DEM") == "DEM"
    assert party_codes.normalize("REP") == "REP"


def test_normalize_full_name():
    assert party_codes.normalize("Democratic") == "DEM"
    assert party_codes.normalize("Republican") == "REP"


def test_normalize_single_letter():
    assert party_codes.normalize("D") == "DEM"
    assert party_codes.normalize("R") == "REP"


def test_normalize_case_insensitive():
    assert party_codes.normalize("democratic") == "DEM"
    assert party_codes.normalize("DEMOCRATIC") == "DEM"
    assert party_codes.normalize("Democratic Party") == "DEM"


def test_normalize_strips_whitespace():
    assert party_codes.normalize("  DEM  ") == "DEM"
    assert party_codes.normalize(" Republican ") == "REP"


def test_normalize_unknown_returns_none():
    assert party_codes.normalize("XYZZY") is None


def test_normalize_empty_returns_none():
    assert party_codes.normalize("") is None
    assert party_codes.normalize(None) is None
