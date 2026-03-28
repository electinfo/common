"""Load JSON and YAML schemas bundled with the package."""

import json
from importlib import resources
from pathlib import Path

import yaml


def _find_repo_schemas() -> Path:
    """Walk upward from this file to find the repo-level schemas/ directory."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        candidate = current / "schemas"
        if candidate.is_dir() and (candidate / "constants.json").is_file():
            return candidate
        current = current.parent
    raise FileNotFoundError("Cannot locate schemas/ directory")


def _load_schema(name: str) -> dict:
    # In a built wheel, schemas are bundled inside the package
    pkg_schemas = resources.files("electinfo_common") / "schemas" / name
    if pkg_schemas.is_file():
        return json.loads(pkg_schemas.read_text(encoding="utf-8"))

    # In an editable install, walk up to find the repo-level schemas/
    return json.loads((_find_repo_schemas() / name).read_text(encoding="utf-8"))


def _load_yaml(name: str) -> dict:
    # In a built wheel, schemas are bundled inside the package
    pkg_schemas = resources.files("electinfo_common") / "schemas" / name
    if pkg_schemas.is_file():
        return yaml.safe_load(pkg_schemas.read_text(encoding="utf-8"))

    # In an editable install, walk up to find the repo-level schemas/
    return yaml.safe_load((_find_repo_schemas() / name).read_text(encoding="utf-8"))


url_patterns: dict = _load_schema("url-patterns.json")
constants: dict = _load_schema("constants.json")
entity_types: dict = _load_schema("entity-types.json")
party_codes: dict = _load_yaml("party-codes.yaml")
state_codes: dict = _load_yaml("state-codes.yaml")
office_codes: dict = _load_yaml("office-codes.yaml")
org_stopwords: dict = _load_yaml("org-stopwords.yaml")
