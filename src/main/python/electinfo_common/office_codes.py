"""Political office code mappings and normalization.

Loads canonical office type codes and alias mappings from office-codes.yaml.
"""

from __future__ import annotations

from electinfo_common._schemas import office_codes as _raw

# Office code → {name, level, branch, has_state, has_district}
federal: dict[str, dict] = _raw["federal"]
state_executive: dict[str, dict] = _raw["state_executive"]
state_legislative: dict[str, dict] = _raw["state_legislative"]
local: dict[str, dict] = _raw["local"]

# Alias (UPPER-CASED variant) → canonical code
aliases: dict[str, str] = _raw["aliases"]

# Convenience: flat code → info for all office types
codes: dict[str, dict] = {
    **federal,
    **state_executive,
    **state_legislative,
    **local,
}

# Convenience: flat code → name
names: dict[str, str] = {code: info["name"] for code, info in codes.items()}


def normalize(value: str) -> str | None:
    """Normalize an office value to its canonical code.

    Accepts canonical codes, abbreviations, or full office names.
    Returns None if no match found.
    """
    if not value:
        return None
    key = value.strip().upper()
    if key in codes:
        return key
    return aliases.get(key)
