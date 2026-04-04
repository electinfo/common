# Entity Types

TypeScript interfaces for all entity types in the elect.info platform. These types match the Neo4j GraphQL API responses and serve as the single source of truth for entity data structure.

## Usage

```typescript
import type { Candidate, Committee, Individual, EntityType } from '@electinfo/common';

// Type-safe entity handling
const candidate: Candidate = {
  id: '123',
  fecId: 'C00001234',
  name: 'John Smith',
  office: 'senate',
  state: 'CA',
  party: 'democratic'
};

// Type guards
import { isCandidate, getEntityType } from '@electinfo/common';

if (isCandidate(entity)) {
  console.log(`${entity.name} is running for ${entity.office}`);
}

const type = getEntityType(entity);
if (type === EntityType.CANDIDATE) {
  // ...
}
```

## Entity Types

### Primary Entities (Enrichable in CMS)

These entities can have curated content (descriptions, photos) in the CMS:

- **Candidate** - Federal election candidate
- **Committee** - Political Action Committee (PAC)
- **Individual** - Donor/contributor (can also be referenced as "Donor")

### Supporting Entities

These provide context and relationships:

- **Office** - Political office (President, Senate seat, House seat)
- **District** - Congressional or electoral district
- **State** - US state or territory
- **Party** - Political party
- **Election** - Federal election cycle

### Relationships

- **Contribution** - A contribution from a donor to a candidate/committee
- **PaginatedResponse** - Wrapper for paginated GraphQL responses
- **GraphQLResponse** - Wrapper for GraphQL query results with error handling

## Type Guards

Three type guard functions help identify entity types at runtime:

```typescript
isCandidate(entity): boolean
isCommittee(entity): boolean
isIndividual(entity): boolean

// Get entity type programmatically
getEntityType(entity): EntityType | null
```

## Neo4j Metadata

All entities include optional Neo4j metadata:

```typescript
entity._labels   // Array of Neo4j labels (e.g., ['Candidate', 'Person'])
entity._elementId // Internal Neo4j element ID
```

These are preserved from GraphQL responses but typically not used in frontend logic.

## Integration with CMS

When you fetch from Payload CMS, the structure extends these base types:

```typescript
// From Neo4j GraphQL
const candidate: Candidate = { ... };

// From Payload CMS (via cms-loader)
const merged: CandidateMerged = {
  ...candidate,  // All GraphQL fields
  curated_description: '...',  // CMS enrichment
  curated_photo: { ... },      // CMS enrichment
  cms_status: 'published',     // CMS metadata
  _source: { graphql: true, cms: true, merged_at: ... }
};
```

See `cms/payload/types/` for CMS-specific extensions.
