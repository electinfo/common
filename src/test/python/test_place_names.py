"""Tests for place_names module."""

import pytest
from electinfo_common.place_names import normalize_place_name, strip_lsad_suffix


class TestStripLsadSuffix:
    """Tests for strip_lsad_suffix."""

    @pytest.mark.parametrize(
        "input_name, expected",
        [
            ("Chicago city", "Chicago"),
            ("Spring Church CDP", "Spring Church"),
            ("Endicott town", "Endicott"),
            ("Darien village", "Darien"),
            ("Mansfield borough", "Mansfield"),
            ("Magna metro township", "Magna"),
            ("Anchorage municipality", "Anchorage"),
            ("Sitka city and borough", "Sitka"),
            ("Lexington-Fayette urban county", "Lexington-Fayette"),
            ("Lynchburg, Moore County metropolitan government", "Lynchburg, Moore County"),
            ("Cusseta-Chattahoochee County unified government", "Cusseta-Chattahoochee County"),
            ("Echols County consolidated government", "Echols County"),
            ("Ranson corporation", "Ranson"),
            ("Lares zona urbana", "Lares"),
            ("Parcelas Viejas Borinquen comunidad", "Parcelas Viejas Borinquen"),
            ("Clifton township", "Clifton"),
        ],
    )
    def test_strips_lsad_suffixes(self, input_name: str, expected: str) -> None:
        assert strip_lsad_suffix(input_name) == expected

    def test_strips_balance_suffix(self) -> None:
        assert strip_lsad_suffix("Nashville-Davidson metropolitan government (balance)") == "Nashville-Davidson"

    def test_strips_balance_with_unified_gov(self) -> None:
        assert strip_lsad_suffix("Greeley County unified government (balance)") == "Greeley County"

    def test_no_suffix(self) -> None:
        assert strip_lsad_suffix("Austin") == "Austin"

    def test_preserves_capitalized_city_in_name(self) -> None:
        """'City' capitalized = part of proper name, not LSAD suffix."""
        assert strip_lsad_suffix("Kansas City") == "Kansas City"
        assert strip_lsad_suffix("Oklahoma City") == "Oklahoma City"
        assert strip_lsad_suffix("Salt Lake City") == "Salt Lake City"

    def test_strips_lowercase_city_after_capitalized_city(self) -> None:
        """Census form: 'Kansas City city' — lowercase 'city' is the LSAD suffix."""
        assert strip_lsad_suffix("Kansas City city") == "Kansas City"
        assert strip_lsad_suffix("Oklahoma City city") == "Oklahoma City"
        assert strip_lsad_suffix("Salt Lake City city") == "Salt Lake City"

    def test_uppercase_input_passthrough(self) -> None:
        """Already-uppercase candidate data passes through unchanged."""
        assert strip_lsad_suffix("KANSAS CITY") == "KANSAS CITY"
        assert strip_lsad_suffix("CHICAGO") == "CHICAGO"
        assert strip_lsad_suffix("LOS ANGELES") == "LOS ANGELES"

    def test_empty_string(self) -> None:
        assert strip_lsad_suffix("") == ""

    def test_none(self) -> None:
        assert strip_lsad_suffix(None) == ""

    def test_whitespace_only(self) -> None:
        assert strip_lsad_suffix("   ") == ""

    def test_trailing_whitespace(self) -> None:
        assert strip_lsad_suffix("Chicago city  ") == "Chicago"


class TestNormalizePlaceName:
    """Tests for normalize_place_name."""

    def test_strips_and_uppercases(self) -> None:
        assert normalize_place_name("Chicago city") == "CHICAGO"

    def test_trims_whitespace(self) -> None:
        assert normalize_place_name("  los angeles city  ") == "LOS ANGELES"

    def test_cdp(self) -> None:
        assert normalize_place_name("Spring Church CDP") == "SPRING CHURCH"

    def test_no_suffix(self) -> None:
        assert normalize_place_name("Austin") == "AUSTIN"

    def test_preserves_city_in_proper_name(self) -> None:
        assert normalize_place_name("Kansas City") == "KANSAS CITY"
        assert normalize_place_name("Kansas City city") == "KANSAS CITY"
        assert normalize_place_name("KANSAS CITY") == "KANSAS CITY"

    def test_none(self) -> None:
        assert normalize_place_name(None) == ""

    def test_empty(self) -> None:
        assert normalize_place_name("") == ""
