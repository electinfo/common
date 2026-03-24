"""Place name normalization for cross-catalog alignment."""

import re

# Census LSAD type suffixes, ordered longest-first to avoid partial matches.
# Source: Census Bureau gazetteer LSAD codes.
# These appear in their original casing from census data — lowercase except
# "CDP" which is always uppercase.
_LSAD_SUFFIXES = [
    "consolidated government",
    "metropolitan government",
    "unified government",
    "city and borough",
    "metro township",
    "zona urbana",
    "municipality",
    "urban county",
    "corporation",
    "comunidad",
    "township",
    "borough",
    "village",
    "city",
    "town",
    "CDP",
]

# Case-SENSITIVE pattern. Census LSAD suffixes are always lowercase
# (except CDP) in the source data, while proper-name words like "City"
# in "Kansas City" are capitalized. This prevents stripping "City"
# from proper names while correctly stripping "city" LSAD suffixes.
_LSAD_PATTERN = re.compile(
    r"\s+(?:" + "|".join(re.escape(s) for s in _LSAD_SUFFIXES) + r")\s*$",
)

# Match "(balance)" suffix (with optional whitespace).
_BALANCE_PATTERN = re.compile(r"\s*\(balance\)\s*$", re.IGNORECASE)


def strip_lsad_suffix(place_name: str) -> str:
    """Strip Census LSAD type suffix from a place name.

    Case-sensitive: only strips lowercase suffixes (matching census
    gazetteer conventions). "Kansas City" is preserved because "City"
    is capitalized, while "Kansas City city" correctly strips the
    lowercase LSAD "city" suffix.

    Examples::

        >>> strip_lsad_suffix("Chicago city")
        'Chicago'
        >>> strip_lsad_suffix("Kansas City city")
        'Kansas City'
        >>> strip_lsad_suffix("Kansas City")
        'Kansas City'
        >>> strip_lsad_suffix("Spring Church CDP")
        'Spring Church'
        >>> strip_lsad_suffix("Nashville-Davidson metropolitan government (balance)")
        'Nashville-Davidson'
        >>> strip_lsad_suffix("Juneau city and borough")
        'Juneau'
        >>> strip_lsad_suffix("Austin")
        'Austin'
        >>> strip_lsad_suffix("")
        ''
        >>> strip_lsad_suffix(None)
        ''
    """
    if not place_name:
        return ""
    result = _BALANCE_PATTERN.sub("", place_name)
    result = _LSAD_PATTERN.sub("", result)
    return result.strip()


def normalize_place_name(place_name: str) -> str:
    """Normalize a place name for cross-catalog matching.

    Strips LSAD suffix (case-sensitive), then uppercases and trims.
    The result is suitable for use as a UUID5 hash key component.

    For census data: strip suffix then uppercase.
    For candidate data (already uppercase, no LSAD suffix): just trims.

    Examples::

        >>> normalize_place_name("Chicago city")
        'CHICAGO'
        >>> normalize_place_name("  los angeles city  ")
        'LOS ANGELES'
        >>> normalize_place_name("Kansas City city")
        'KANSAS CITY'
        >>> normalize_place_name("Kansas City")
        'KANSAS CITY'
        >>> normalize_place_name("KANSAS CITY")
        'KANSAS CITY'
        >>> normalize_place_name("Spring Church CDP")
        'SPRING CHURCH'
        >>> normalize_place_name(None)
        ''
    """
    return strip_lsad_suffix(place_name).upper().strip()
