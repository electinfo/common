# common - Shared Schemas and Constants

> **SESSION START**: Always read all markdown files in ALL electinfo repositories at session start:
> ```
> ~/git/electinfo/CLAUDE.md
> ~/git/electinfo/*/CLAUDE.md
> ~/git/electinfo/docs/*.md
> ~/git/electinfo/rundeck/ROADMAP.md
> ```

Shared schemas, templates, and constants for the electinfo platform. Published to npm (TypeScript/JavaScript), Maven (Scala/Java), and PyPI (Python).

## Purpose

This repository ensures consistency across the electinfo platform by providing:

1. **URL Patterns** - Canonical patterns for entity page URLs
2. **Constants** - State names, party codes, committee types, etc.
3. **JSON Schemas** - Validation schemas for data structures
4. **Templates** - Shared HTML/Mustache templates (future)

## Repository Structure

```
common/
├── CLAUDE.md              # This file
├── package.json           # npm package config
├── build.sbt              # sbt/Maven config
├── tsconfig.json          # TypeScript config
├── pyproject.toml         # Python package config (hatchling)
├── schemas/               # JSON schemas
│   ├── url-patterns.json  # Entity URL patterns
│   └── constants.json     # Shared constants
├── templates/             # Shared templates (future)
└── src/
    ├── main/
    │   ├── typescript/
    │   │   └── index.ts           # TypeScript exports
    │   ├── python/
    │   │   └── electinfo_common/
    │   │       ├── __init__.py    # Public API
    │   │       ├── _schemas.py    # JSON schema loading
    │   │       ├── constants.py   # Constants class
    │   │       ├── url_patterns.py# UrlPatterns class
    │   │       ├── slug.py        # make_slug()
    │   │       └── py.typed       # PEP 561 marker
    │   └── scala/                 # (future: Scala wrappers)
    └── test/
        └── python/
            ├── test_constants.py
            ├── test_slug.py
            └── test_url_patterns.py
```

## Publishing

### npm (TypeScript/JavaScript)

Published to: `https://repo.elect.info/repository/npm-hosted/`

```bash
npm publish
```

Consumers:
```bash
npm install @electinfo/common --registry https://repo.elect.info/repository/npm-group/
```

### Maven (Scala/Java)

Published to: `https://repo.elect.info/repository/maven-releases/`

```bash
sbt publish
```

Consumers (build.sbt):
```scala
libraryDependencies += "info.elect" %% "electinfo-common" % "0.1.0"
resolvers += "Nexus" at "https://repo.elect.info/repository/maven-public/"
```

### PyPI (Python)

Published to: `https://repo.elect.info/repository/pypi-hosted/`

```bash
python -m build
twine upload --repository-url https://repo.elect.info/repository/pypi-hosted/ dist/*
```

Consumers:
```bash
pip install electinfo-common --index-url https://repo.elect.info/repository/pypi-group/simple/
```

## Usage

### TypeScript

```typescript
import { UrlPatterns, Constants } from '@electinfo/common';

// Generate candidate URL
const url = UrlPatterns.candidate.senate('ca', 'john-smith');
// => "/candidates/senate/ca/john-smith/"

// Get state name
const name = Constants.stateNames['CA'];
// => "California"
```

### Python

```python
from electinfo_common import UrlPatterns, Constants, make_slug

# Generate candidate URL
url = UrlPatterns.candidate.senate("ca", "john-smith")
# => "/candidates/senate/ca/john-smith/"

# Get state name
name = Constants.state_names["CA"]
# => "California"

# Generate slug
slug = make_slug("John Smith")
# => "john-smith"
```

### Scala

```scala
import info.elect.common.{UrlPatterns, Constants}

// Generate candidate URL
val url = UrlPatterns.candidate.senate("ca", "john-smith")
// => "/candidates/senate/ca/john-smith/"

// Get state name
val name = Constants.stateNames("CA")
// => "California"
```

## Development

### Python

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest src/test/python/ -v
```

### TypeScript

```bash
# Install dependencies
npm install

# Type-check
npx tsc --noEmit
```

## CI/CD

Tekton pipeline triggers on push to main:
1. Runs tests
2. Publishes to npm (repo.elect.info)
3. Publishes to Maven (repo.elect.info)
4. Publishes to PyPI (repo.elect.info)

## Adoption Plan

### Phase 1: Bootstrap (Current)
- [x] Create repository structure
- [x] Define URL patterns schema
- [x] Define constants schema
- [x] Add TypeScript exports
- [x] Add Python package with tests
- [ ] Add Scala resource loading
- [ ] Set up Tekton pipeline
- [ ] Initial publish to npm, Maven, and PyPI

### Phase 2: Migrate rundeck
- [ ] Update Constants.scala to read from common
- [ ] Update templates.py to use electinfo-common
- [ ] Remove duplicate constant definitions
- [ ] Test static page generation

### Phase 3: Migrate sites
- [ ] Update base.ts to import from @electinfo/common
- [ ] Update entity index TypeScript files
- [ ] Remove duplicate constant definitions
- [ ] Test search result URLs

### Phase 4: Validation
- [ ] Add pre-commit hooks to validate URL consistency
- [ ] Add integration tests comparing generated URLs
- [ ] Document migration in CLAUDE.md files

## Related Repositories

| Repository | Uses common for |
|------------|-----------------|
| rundeck | Static page URL generation (Scala + Python) |
| sites | Search result URL generation (TypeScript) |
| graphql-server | Entity URL fields (TypeScript) |
