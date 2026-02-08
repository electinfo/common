"""Canonical URL pattern generators for electinfo entity pages."""

from __future__ import annotations

import re


class _CandidatePatterns:
    """URL generators for candidate pages."""

    @staticmethod
    def president(slug: str) -> str:
        return f"/candidates/president/us/{slug}/"

    @staticmethod
    def senate(state: str, slug: str) -> str:
        return f"/candidates/senate/{state.lower()}/{slug}/"

    @staticmethod
    def house(state: str, district: str | int, slug: str) -> str:
        district_padded = str(district).zfill(2)
        return f"/candidates/house/{state.lower()}-{district_padded}/{slug}/"


class UrlPatterns:
    """Canonical URL generators mirroring the TypeScript API.

    Example::

        UrlPatterns.candidate.senate("ca", "john-smith")
        # => "/candidates/senate/ca/john-smith/"
    """

    candidate = _CandidatePatterns()

    @staticmethod
    def committee(type_slug: str, slug: str, fec_id: str) -> str:
        return f"/committees/{type_slug}/{slug}-{fec_id.lower()}/"

    @staticmethod
    def individual(slug: str, hash_id: str) -> str:
        id_clean = re.sub(r"^I-", "", hash_id, flags=re.IGNORECASE).lower()
        id_suffix = id_clean[:12]
        return f"/individuals/{slug}-i-{id_suffix}/"

    @staticmethod
    def employer(slug: str, hash_id: str) -> str:
        id_clean = re.sub(r"^O-", "", hash_id, flags=re.IGNORECASE).lower()
        return f"/employers/{slug}-{id_clean}/"

    @staticmethod
    def vendor(slug: str, hash_id: str) -> str:
        id_clean = re.sub(r"^V-", "", hash_id, flags=re.IGNORECASE).lower()
        return f"/vendors/{slug}-{id_clean}/"

    @staticmethod
    def party(slug: str) -> str:
        return f"/parties/{slug}/"

    @staticmethod
    def district(slug: str) -> str:
        return f"/districts/{slug}/"

    @staticmethod
    def state(slug: str) -> str:
        return f"/states/{slug}/"

    @staticmethod
    def cycle(year: int | str) -> str:
        return f"/elections/{year}/"
