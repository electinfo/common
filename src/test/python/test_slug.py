from electinfo_common import make_slug


def test_basic_slug():
    assert make_slug("John Smith") == "john-smith"


def test_empty_string():
    assert make_slug("") == ""


def test_special_characters():
    assert make_slug("O'Brien-Jones") == "obrien-jones"


def test_multiple_spaces():
    assert make_slug("  John   Smith  ") == "john-smith"


def test_already_slug():
    assert make_slug("john-smith") == "john-smith"


def test_uppercase():
    assert make_slug("JOHN SMITH") == "john-smith"


def test_numbers():
    assert make_slug("District 12") == "district-12"
