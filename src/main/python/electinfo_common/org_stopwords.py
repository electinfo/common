"""Organization name leading stopwords.

Loads the canonical list of leading stopwords from org-stopwords.yaml.
These are stripped from the beginning of organization names before UUID5
ID computation, ensuring variants like "THE COCA COLA" and "COCA COLA"
resolve to the same entity.
"""

from __future__ import annotations

from electinfo_common._schemas import org_stopwords as _raw

# Words to strip from the beginning of org names (UPPER-CASE)
leading: list[str] = _raw["leading"]

# Frozen set for O(1) membership tests
leading_set: frozenset[str] = frozenset(leading)
