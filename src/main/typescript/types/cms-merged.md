# CMS-Merged Entity Types

Type definitions for entities enriched with Payload CMS editorial content.

## Overview

CMS-merged types extend Neo4j entity types with editorial content from Payload CMS:

```typescript
import {
  CandidateMerged,
  CommitteeMerged,
  IndividualMerged,
  isCandidateMerged,
} from '@electinfo/common';

// Fetch merged data
const candidate: CandidateMerged = {
  // Neo4j fields (extends Candidate)
  id: 'neo4j-id',
  fecId: 'C00123456',
  name: 'John Smith',
  office: 'senate',
  party: 'democratic',

  // CMS fields
  cmsId: 'payload-doc-id',
  description: 'Curated biography of John Smith...',
  photo: {
    url: '/media/candidates/john-smith.jpg',
    alt: 'John Smith',
    caption: 'Official campaign photo',
  },

  // Editorial metadata
  editorial: {
    status: 'published',
    lastCuratedBy: 'editor@elect.info',
    lastCuratedAt: '2026-01-15T10:30:00Z',
    verifiedAt: '2026-01-15T10:30:00Z',
    internalNotes: 'Verified with official campaign website',
  },

  // Data source tracking
  _dataSource: {
    graphql: ['id', 'fecId', 'name', 'office', 'party', ...],
    cms: ['cmsId', 'description', 'photo', 'editorial'],
    mergedAt: '2026-04-04T14:30:00Z',
  },
};
```

## Type Definitions

### `CandidateMerged`

Extends `Candidate` with CMS enrichment.

**Neo4j fields** (from `Candidate`):
- `id: string` - Neo4j node ID
- `fecId: string` - FEC candidate ID
- `name: string` - Full name
- `office: 'president' | 'senate' | 'house'` - Office sought
- `state?: string` - State (2-letter code)
- `district?: string` - Congressional district (House only)
- `party: 'democratic' | 'republican' | ...` - Party affiliation
- `websiteUrl?: string` - Campaign website
- `email?: string` - Email address
- `phone?: string` - Phone number
- `crpId?: string` - Center for Responsive Politics ID
- `bioguideId?: string` - Congressional Bioguide ID
- `_labels?: string[]` - Neo4j labels
- `_elementId?: string` - Neo4j element ID

**CMS fields**:
- `cmsId?: string` - Payload CMS document ID
- `description?: string` - Rich text biography/editorial description
- `photo?: { url: string; alt?: string; caption?: string }` - Campaign photo with metadata

**Editorial metadata**:
- `editorial?: { ... }` - CMS editorial status and tracking
  - `status: 'draft' | 'published' | 'archived'` - Document status
  - `lastCuratedBy?: string` - Email of last editor
  - `lastCuratedAt?: string` - ISO 8601 timestamp of last update
  - `verifiedAt?: string` - ISO 8601 timestamp of verification
  - `internalNotes?: string` - Internal editorial notes

**Data source tracking**:
- `_dataSource?: { graphql: string[]; cms: string[]; mergedAt: string }` - Source tracking (only if `includeDataSource` is true)

### `CommitteeMerged`

Extends `Committee` with CMS enrichment.

**Neo4j fields** (from `Committee`):
- `id: string` - Neo4j node ID
- `fecId: string` - FEC committee ID
- `name: string` - Committee name
- `type: 'pac' | 'super-pac' | 'party' | 'hybrid' | 'leadership' | 'other'` - Committee type
- `state?: string` - State (2-letter code)
- `treasurer?: string` - Treasurer name
- `treasurerPhone?: string` - Treasurer phone
- `treasurerEmail?: string` - Treasurer email
- `designationCode?: string` - FEC designation code
- `crpId?: string` - Center for Responsive Politics ID
- `_labels?: string[]` - Neo4j labels
- `_elementId?: string` - Neo4j element ID

**CMS fields**:
- `cmsId?: string` - Payload CMS document ID
- `description?: string` - Rich text committee description
- `logo?: { url: string; alt?: string }` - Committee logo

**Editorial metadata** and **data source tracking** same as `CandidateMerged`.

### `IndividualMerged`

Extends `Individual` with CMS enrichment.

**Neo4j fields** (from `Individual`):
- `id: string` - Neo4j node ID
- `name: string` - Full name
- `address?: string` - Street address
- `city?: string` - City
- `state?: string` - State (2-letter code)
- `zip?: string` - ZIP code
- `employer?: string` - Employer name
- `occupation?: string` - Occupation
- `_labels?: string[]` - Neo4j labels
- `_elementId?: string` - Neo4j element ID

**CMS fields**:
- `cmsId?: string` - Payload CMS document ID
- `biography?: string` - Rich text biography
- `photo?: { url: string; alt?: string }` - Person's photo

**Editorial metadata** and **data source tracking** same as `CandidateMerged`.

## Type Guards

Type guard functions for runtime type checking:

### `isCandidateMerged(entity)`

```typescript
function isCandidateMerged(entity: unknown): entity is CandidateMerged
```

Checks if entity is a valid `CandidateMerged` object.

```typescript
const data = await loader.getCandidate('C00123456');

if (isCandidateMerged(data)) {
  // TypeScript knows `data` is CandidateMerged
  console.log(data.description);
} else {
  console.log('Not a valid candidate');
}
```

### `isCommitteeMerged(entity)`

```typescript
function isCommitteeMerged(entity: unknown): entity is CommitteeMerged
```

### `isIndividualMerged(entity)`

```typescript
function isIndividualMerged(entity: unknown): entity is IndividualMerged
```

## Data Merging Rules

### Priority

By default, Neo4j (GraphQL) data takes priority:

```typescript
// If both GraphQL and CMS provide a value
const candidate = {
  name: 'John Smith (from GraphQL)',  // <-- GraphQL wins
  description: 'Bio from CMS...',     // <-- CMS wins (GraphQL has no description)
};
```

Use `cmsPriority` option to prefer CMS:

```typescript
const merged = await loader.getCandidate('C00123456', {
  cmsPriority: true,
});
// Now CMS values override GraphQL when both exist
```

### Draft vs Published

By default, draft CMS documents are included:

```typescript
const candidate = await loader.getCandidate('C00123456');
// Merged even if CMS document is draft
```

Use `onlyPublished` to skip draft documents:

```typescript
const published = await loader.getCandidate('C00123456', {
  onlyPublished: true,
});
// Returns GraphQL-only data if CMS document is not published
```

### Null/Undefined Handling

- If CMS field is `null` or `undefined`, GraphQL field is preserved
- If GraphQL field is missing, CMS field is included
- GraphQL fields always exist (they're authoritative)
- CMS fields are optional enrichment

```typescript
const candidate: CandidateMerged = {
  // Always from GraphQL (required)
  id: 'neo4j-id',
  fecId: 'C00123456',
  name: 'John Smith',

  // Optional CMS enrichment
  description: undefined,  // <-- Merged, but undefined
  cmsId: undefined,        // <-- Not included if undefined
};
```

## Data Source Tracking

When `includeDataSource` is true (default), each merged entity includes:

```typescript
_dataSource: {
  graphql: ['id', 'fecId', 'name', 'office', ...],  // Fields from Neo4j
  cms: ['cmsId', 'description', 'photo', 'editorial'],  // Fields from CMS
  mergedAt: '2026-04-04T14:30:00Z',  // UTC timestamp
}
```

Use data source tracking to:

1. **Debug** - See which fields came from where
2. **Attribution** - Display sources to users
3. **Fallback** - Handle missing data gracefully
4. **Metrics** - Track CMS enrichment rates

```typescript
if (candidate._dataSource?.cms.includes('description')) {
  // CMS provided a description
  showCuratedLabel();
}

if (!candidate._dataSource?.cms.includes('photo')) {
  // Photo came from GraphQL or missing
  useFallbackPhoto();
}
```

## Common Patterns

### Type-safe access with guards

```typescript
const data = await loader.getCandidate(id);

if (isCandidateMerged(data)) {
  console.log(data.description);      // Safe to access
  console.log(data.editorial?.status); // Safe to access optional editorial
} else if (!data) {
  console.log('Not found');
} else {
  console.log('Invalid type');
}
```

### Conditional rendering

```typescript
interface CandidateCardProps {
  candidate: CandidateMerged;
}

function CandidateCard({ candidate }: CandidateCardProps) {
  return (
    <div>
      <h1>{candidate.name}</h1>

      {/* Curated description from CMS */}
      {candidate.description && (
        <div className="description">
          {candidate.description}
        </div>
      )}

      {/* Campaign photo from CMS */}
      {candidate.photo && (
        <img
          src={candidate.photo.url}
          alt={candidate.photo.alt || candidate.name}
        />
      )}

      {/* Editorial metadata */}
      {candidate.editorial?.status === 'published' && (
        <div className="verified">Verified by editors</div>
      )}
    </div>
  );
}
```

### Batch loading with error handling

```typescript
const candidateIds = ['C00123456', 'C00234567', 'C00345678'];

const results = await Promise.allSettled(
  candidateIds.map(id => loader.getCandidate(id))
);

const merged = results
  .map((result, i) => ({
    id: candidateIds[i],
    candidate: result.status === 'fulfilled' ? result.value : null,
    error: result.status === 'rejected' ? result.reason : null,
  }))
  .filter(r => r.candidate);
```

## Migration from GraphQL-only

If migrating from pure GraphQL queries to merged data:

**Before:**
```typescript
const candidate = await fetchFromGraphQL('C00123456');
console.log(candidate.name); // All fields from GraphQL
```

**After:**
```typescript
const loader = createCMSLoader(graphqlUrl, cmsUrl);
const candidate = await loader.getCandidate('C00123456');
console.log(candidate.name);  // Same field, from GraphQL
console.log(candidate.description); // New field, from CMS
```

The `CandidateMerged` type is backwards compatible — it includes all original `Candidate` fields, so existing code continues to work.
