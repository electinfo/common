# common - Shared Schemas and Constants

> **SESSION START**: Always read all markdown files in ALL electinfo repositories at session start:
> ```
> ~/git/electinfo/CLAUDE.md
> ~/git/electinfo/*/CLAUDE.md
> ~/git/electinfo/docs/*.md
> ~/git/electinfo/rundeck/ROADMAP.md
> ```

Shared schemas, templates, and constants for the electinfo platform. Published to both Maven (for Scala/Java) and npm (for TypeScript/JavaScript).

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
├── schemas/               # JSON schemas
│   ├── url-patterns.json  # Entity URL patterns
│   └── constants.json     # Shared constants
├── templates/             # Shared templates (future)
└── src/                   # TypeScript source
    └── index.ts           # Main exports
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

## CI/CD

Tekton pipeline triggers on push to main:
1. Runs tests
2. Publishes to npm (repo.elect.info)
3. Publishes to Maven (repo.elect.info)

## Adoption Plan

### Phase 1: Bootstrap (Current)
- [x] Create repository structure
- [x] Define URL patterns schema
- [x] Define constants schema
- [ ] Add TypeScript exports
- [ ] Add Scala resource loading
- [ ] Set up Tekton pipeline
- [ ] Initial publish to npm and Maven

### Phase 2: Migrate rundeck
- [ ] Update Constants.scala to read from common
- [ ] Update templates.py to read from common
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
| rundeck | Static page URL generation (Scala) |
| sites | Search result URL generation (TypeScript) |
| graphql-server | Entity URL fields (TypeScript) |