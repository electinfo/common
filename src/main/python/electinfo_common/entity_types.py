"""Entity type registry and canonical path generation."""

from __future__ import annotations

from electinfo_common._schemas import entity_types as _raw

_ENTITY_TYPES: dict[str, dict[str, str]] = _raw["entityTypes"]


def canonical_path(entity_type: str, entity_id: str) -> str:
    """Return the canonical path for an entity: {plural}/{id.lower()}.

    >>> canonical_path("Candidate", "P80000722")
    'candidates/p80000722'
    >>> canonical_path("Committee", "C00401224")
    'committees/c00401224'
    """
    config = _ENTITY_TYPES.get(entity_type)
    if config is None:
        raise ValueError(f"Unknown entity type: {entity_type}")
    return f"{config['plural']}/{entity_id.lower()}"
