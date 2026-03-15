"""US state and territory code mappings.

Loads state codes, names, FIPS codes, and aliases from state-codes.yaml.
"""

from __future__ import annotations

from electinfo_common._schemas import state_codes as _raw

# State code → {fips, name, house_seats}
states: dict[str, dict] = _raw["states"]

# Territory code → {fips, name, house_seats}
territories: dict[str, dict] = _raw["territories"]

# Special pseudo-states (e.g. US)
special: dict[str, dict] = _raw.get("special", {})

# Alias (UPPER-CASED full name) → 2-letter code
aliases: dict[str, str] = _raw["aliases"]

# Convenience: flat code → name for all states + territories + special
names: dict[str, str] = {
    **{code: info["name"] for code, info in states.items()},
    **{code: info["name"] for code, info in territories.items()},
    **{code: info["name"] for code, info in special.items()},
}

# Convenience: FIPS → code
fips_to_code: dict[str, str] = {
    **{info["fips"]: code for code, info in states.items()},
    **{info["fips"]: code for code, info in territories.items()},
}

# Convenience: code → house_seats (2020 apportionment)
house_seats: dict[str, int] = {
    **{code: info["house_seats"] for code, info in states.items()},
    **{code: info["house_seats"] for code, info in territories.items()},
}


def normalize(value: str) -> str | None:
    """Normalize a state value to its canonical 2-letter code.

    Accepts 2-letter codes, full state names, or FIPS codes.
    Returns None if no match found.
    """
    if not value:
        return None
    key = value.strip().upper()
    if key in states or key in territories or key in special:
        return key
    if key in aliases:
        return aliases[key]
    # Try FIPS code lookup (2-digit zero-padded)
    fips_key = key.zfill(2) if key.isdigit() else key
    if fips_key in fips_to_code:
        return fips_to_code[fips_key]
    return None
