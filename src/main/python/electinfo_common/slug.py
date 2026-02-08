"""Slug generation matching TypeScript/Scala implementations."""

import re


def make_slug(name: str) -> str:
    """Convert a display name to a URL-safe slug.

    Mirrors the TypeScript ``makeSlug`` function:
    lowercase, strip non-alphanumeric (except spaces/hyphens),
    collapse whitespace to single hyphens, trim leading/trailing hyphens.
    """
    if not name:
        return ""
    s = name.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s
