"""Party code mappings and normalization.

Loads canonical FEC party codes and alias mappings from party-codes.yaml.
"""

from __future__ import annotations

from electinfo_common._schemas import party_codes as _raw

# Canonical FEC code → full party name
codes: dict[str, str] = _raw["codes"]

# Alias (UPPER-CASED variant) → canonical FEC code
aliases: dict[str, str] = _raw["aliases"]


def normalize(value: str) -> str | None:
    """Normalize a party value to its canonical FEC code.

    Applies UPPER + STRIP, then checks canonical codes first,
    then aliases. Returns None if no match found.
    """
    if not value:
        return None
    key = value.strip().upper()
    if key in codes:
        return key
    return aliases.get(key)
