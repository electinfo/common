from electinfo_common import Constants


def test_state_names_has_all_50_states_plus_territories():
    assert len(Constants.state_names) >= 50


def test_state_name_lookup():
    assert Constants.state_names["CA"] == "California"
    assert Constants.state_names["NY"] == "New York"
    assert Constants.state_names["DC"] == "District of Columbia"


def test_party_names():
    assert Constants.party_names["DEM"] == "Democratic Party"
    assert Constants.party_names["REP"] == "Republican Party"


def test_office_names():
    assert Constants.office_names["P"] == "President"
    assert Constants.office_names["S"] == "Senate"
    assert Constants.office_names["H"] == "House"


def test_committee_type_slugs():
    assert Constants.committee_type_slugs["O"] == "super-pac"
    assert Constants.committee_type_slugs["X"] == "party"


def test_committee_type_names():
    assert Constants.committee_type_names["O"] == "Super PAC"


def test_incumbent_status():
    assert Constants.incumbent_status["I"] == "Incumbent"
    assert Constants.incumbent_status["C"] == "Challenger"
    assert Constants.incumbent_status["O"] == "Open Seat"
