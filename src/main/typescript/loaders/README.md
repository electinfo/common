# CMS Data Loaders

Shared TypeScript libraries for loading entity data from Neo4j GraphQL and Payload CMS, with automatic merging and caching.

## cms-loader

Provides the `CMSLoader` class and related utilities for fetching and merging entity data from multiple sources.

### Installation

```bash
npm install @electinfo/common
```

### Basic Usage

```typescript
import { createCMSLoader } from '@electinfo/common';

// Create a loader instance
const loader = createCMSLoader(
  'http://localhost:4000/graphql',      // Neo4j GraphQL endpoint
  'http://localhost:3000/api',           // Payload CMS API endpoint
  {
    cache: 'memory',                      // Enable in-memory caching
    cacheMaxAge: 5 * 60 * 1000,          // 5 minutes
  }
);

// Fetch merged candidate data
const candidate = await loader.getCandidate('john-smith-c00123456', {
  includeDataSource: true,              // Track which fields come from which source
  onlyPublished: true,                  // Only merge published CMS documents
});

console.log(candidate.name);            // From Neo4j
console.log(candidate.description);     // From Payload CMS (if available)
console.log(candidate._dataSource);     // Which fields came from where
```

### API

#### `createCMSLoader(graphqlEndpoint, cmsEndpoint, options?)`

Factory function to create a configured `CMSLoader` instance.

**Parameters:**
- `graphqlEndpoint` (string) - URL to Neo4j GraphQL endpoint
- `cmsEndpoint` (string) - URL to Payload CMS API endpoint
- `options` (CMSLoaderConfig, optional)
  - `timeout` (number) - Request timeout in ms (default: 10000)
  - `cache` ('memory' | 'localStorage' | 'none') - Caching strategy (default: 'memory')
  - `cacheMaxAge` (number) - Cache entry lifetime in ms (default: 5 minutes)

**Returns:** `CMSLoader` instance

#### `CMSLoader.getCandidate(id, options?)`

Fetch and merge candidate data from GraphQL and CMS.

**Parameters:**
- `id` (string) - Candidate ID (FEC ID or Neo4j ID)
- `options` (MergeOptions, optional)
  - `includeDataSource` (boolean) - Include `_dataSource` tracking (default: true)
  - `cmsPriority` (boolean) - Prefer CMS values over GraphQL (default: false)
  - `onlyPublished` (boolean) - Only merge published CMS documents (default: false)

**Returns:** `Promise<CandidateMerged | null>`

#### `CMSLoader.getCommittee(id, options?)`

Fetch and merge committee data from GraphQL and CMS.

**Parameters:**
- `id` (string) - Committee ID (FEC ID or Neo4j ID)
- `options` (MergeOptions, optional)

**Returns:** `Promise<CommitteeMerged | null>`

#### `CMSLoader.getIndividual(id, options?)`

Fetch and merge individual data from GraphQL and CMS.

**Parameters:**
- `id` (string) - Individual ID (Neo4j ID)
- `options` (MergeOptions, optional)

**Returns:** `Promise<IndividualMerged | null>`

#### `CMSLoader.clearCache()`

Clear all cached data.

**Returns:** `void`

### Type Definitions

#### `CandidateMerged`

Extends `Candidate` with CMS enrichment:

```typescript
interface CandidateMerged extends Candidate {
  // From CMS
  cmsId?: string;
  description?: string;
  photo?: {
    url: string;
    alt?: string;
    caption?: string;
  };
  editorial?: {
    status: 'draft' | 'published' | 'archived';
    lastCuratedBy?: string;
    lastCuratedAt?: string;
    verifiedAt?: string;
    internalNotes?: string;
  };
  // Data source tracking
  _dataSource?: {
    graphql: string[];   // Fields from Neo4j
    cms: string[];       // Fields from Payload
    mergedAt: string;    // When merge occurred
  };
}
```

#### `CommitteeMerged`

Extends `Committee` with CMS enrichment (similar structure to `CandidateMerged`).

#### `IndividualMerged`

Extends `Individual` with CMS enrichment (similar structure to `CandidateMerged`).

### Usage Examples

#### Fetch with data source tracking

```typescript
const candidate = await loader.getCandidate('C00123456', {
  includeDataSource: true,
});

// Which fields came from GraphQL?
console.log(candidate._dataSource?.graphql);
// => ['id', 'fecId', 'name', 'office', 'state', 'party', ...]

// Which fields came from CMS?
console.log(candidate._dataSource?.cms);
// => ['cmsId', 'description', 'photo', 'editorial']
```

#### Only use published CMS content

```typescript
const candidate = await loader.getCandidate('C00123456', {
  onlyPublished: true,
});

// If CMS document is not published, it will not be merged
// Result contains GraphQL data only
```

#### Disable caching for fresh data

```typescript
const loader = createCMSLoader(
  graphqlEndpoint,
  cmsEndpoint,
  { cache: 'none' }
);

// Each call will fetch from both APIs
const candidate1 = await loader.getCandidate('C00123456');
const candidate2 = await loader.getCandidate('C00123456'); // Fresh fetch
```

#### Clear cache

```typescript
// After initial load
const candidate = await loader.getCandidate('C00123456');

// Clear all cached data
loader.clearCache();

// Next call will fetch fresh data
const updated = await loader.getCandidate('C00123456');
```

### Parallel Fetching

The loader automatically fetches from both Neo4j and CMS in parallel:

```typescript
// This makes two concurrent requests
const candidate = await loader.getCandidate('C00123456');
// ~10ms total (if both endpoints respond in ~10ms)
// vs ~20ms if fetched sequentially
```

### Error Handling

The loader gracefully handles errors:

```typescript
try {
  const candidate = await loader.getCandidate('C00123456');

  if (!candidate) {
    console.log('Candidate not found in GraphQL');
    return;
  }

  // Use merged data
  console.log(candidate.name, candidate.description);
} catch (error) {
  if (error instanceof TypeError && error.message.includes('fetch')) {
    console.error('Network error:', error);
  } else {
    console.error('Unexpected error:', error);
  }
}
```

### Caching Strategies

#### Memory Cache (Default)

In-memory caching suitable for single-page applications:

```typescript
const loader = createCMSLoader(
  graphqlEndpoint,
  cmsEndpoint,
  {
    cache: 'memory',
    cacheMaxAge: 5 * 60 * 1000,  // 5 minutes
  }
);
```

**Pros:** Fast, no dependencies, automatic expiration
**Cons:** Lost on page refresh, per-instance cache

#### LocalStorage Cache

Browser persistent caching:

```typescript
const loader = createCMSLoader(
  graphqlEndpoint,
  cmsEndpoint,
  {
    cache: 'localStorage',
    cacheMaxAge: 60 * 60 * 1000,  // 1 hour
  }
);
```

**Pros:** Persists across page refreshes, automatic expiration
**Cons:** Shared across tabs, limited size (~5-10MB)

#### No Cache

Disable caching for always-fresh data:

```typescript
const loader = createCMSLoader(
  graphqlEndpoint,
  cmsEndpoint,
  { cache: 'none' }
);
```

**Pros:** Always current data
**Cons:** Slower, more network requests

### Integration with Frontend Frameworks

#### React

```typescript
import { useMemo, useEffect, useState } from 'react';
import { createCMSLoader } from '@electinfo/common';

function CandidateDetail({ candidateId }: { candidateId: string }) {
  const [candidate, setCandidate] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loader = useMemo(
    () => createCMSLoader(
      'http://api.elect.info/graphql',
      'http://cms.elect.info/api'
    ),
    []
  );

  useEffect(() => {
    loader.getCandidate(candidateId)
      .then(setCandidate)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [candidateId, loader]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!candidate) return <div>Not found</div>;

  return (
    <div>
      <h1>{candidate.name}</h1>
      <p>{candidate.description}</p>
      {candidate.photo && <img src={candidate.photo.url} alt={candidate.photo.alt} />}
    </div>
  );
}
```

#### Next.js (Server-side)

```typescript
import { createCMSLoader } from '@electinfo/common';

export async function getCandidateData(candidateId: string) {
  const loader = createCMSLoader(
    'http://api.elect.info/graphql',
    'http://cms.elect.info/api'
  );

  return loader.getCandidate(candidateId, {
    includeDataSource: false,
    onlyPublished: true,
  });
}
```

### Performance Considerations

1. **Parallel requests** - GraphQL and CMS requests happen concurrently, reducing total latency
2. **Caching** - Reduces repeated requests to both endpoints; configure `cacheMaxAge` based on update frequency
3. **Timeout** - Default 10s timeout prevents hanging requests; adjust based on endpoint performance
4. **Batch operations** - For multiple entities, consider using Promise.all with the loader

```typescript
// Load multiple candidates in parallel
const candidateIds = ['C00123456', 'C00234567', 'C00345678'];
const candidates = await Promise.all(
  candidateIds.map(id => loader.getCandidate(id))
);
```

### Testing

Type guards for testing merged data:

```typescript
import { isCandidateMerged, isCommitteeMerged } from '@electinfo/common';

const data = await loader.getCandidate('C00123456');

if (isCandidateMerged(data)) {
  // TypeScript knows `data` is CandidateMerged
  console.log(data.description); // OK
  console.log(data._dataSource);  // OK
}
```
