"""Shared constants for the electinfo platform."""

from __future__ import annotations

from electinfo_common._schemas import constants as _raw


class Constants:
    """Typed access to electinfo constants.

    Attributes use snake_case per PEP 8 (e.g. ``state_names`` not ``stateNames``).
    """

    state_names: dict[str, str] = _raw["stateNames"]
    party_names: dict[str, str] = _raw["partyNames"]
    office_names: dict[str, str] = _raw["officeNames"]
    committee_type_slugs: dict[str, str] = _raw["committeeTypeSlugs"]
    committee_type_names: dict[str, str] = _raw["committeeTypeNames"]
    incumbent_status: dict[str, str] = _raw["incumbentStatus"]
