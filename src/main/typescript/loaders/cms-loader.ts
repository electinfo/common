/**
 * CMS Data Loader
 *
 * Provides functions to:
 * - Fetch entity data from Neo4j GraphQL and Payload CMS in parallel
 * - Merge results with proper type composition
 * - Handle caching and error scenarios
 * - Track which fields come from which source
 */

import type {
  Candidate,
  Committee,
  Individual,
  EntityType,
} from '../types/entities';
import type {
  CandidateMerged,
  CommitteeMerged,
  IndividualMerged,
} from '../types/cms-merged';

/**
 * GraphQL API Response Types
 */
interface GraphQLResponse<T> {
  data?: {
    [key: string]: T | T[];
  };
  errors?: Array<{ message: string }>;
}

/**
 * Payload CMS API Response Types
 */
interface PayloadResponse<T> {
  doc?: T;
  docs?: T[];
  totalDocs?: number;
  hasNextPage?: boolean;
  hasPrevPage?: boolean;
  page?: number;
  totalPages?: number;
  pagingCounter?: number;
  prevPage?: number;
  nextPage?: number;
}

/**
 * Loader Configuration
 */
export interface CMSLoaderConfig {
  graphqlEndpoint: string;
  cmsEndpoint: string;
  timeout?: number;
  cache?: 'memory' | 'localStorage' | 'none';
  cacheMaxAge?: number; // milliseconds
}

/**
 * Merge Options
 */
export interface MergeOptions {
  /** Include data source tracking in merged result */
  includeDataSource?: boolean;
  /** Prefer CMS values over GraphQL when both exist */
  cmsPriority?: boolean;
  /** Only merge published CMS documents */
  onlyPublished?: boolean;
}

/**
 * Cache Storage
 */
interface CacheEntry<T> {
  data: T;
  timestamp: number;
}

class MemoryCache {
  private cache = new Map<string, CacheEntry<any>>();
  private maxAge: number;

  constructor(maxAge: number = 5 * 60 * 1000) {
    // 5 minutes default
    this.maxAge = maxAge;
  }

  get<T>(key: string): T | null {
    const entry = this.cache.get(key);
    if (!entry) return null;

    if (Date.now() - entry.timestamp > this.maxAge) {
      this.cache.delete(key);
      return null;
    }

    return entry.data as T;
  }

  set<T>(key: string, data: T): void {
    this.cache.set(key, {
      data,
      timestamp: Date.now(),
    });
  }

  clear(): void {
    this.cache.clear();
  }
}

/**
 * CMS Loader Class
 */
export class CMSLoader {
  private config: CMSLoaderConfig;
  private cache: MemoryCache | null = null;

  constructor(config: CMSLoaderConfig) {
    this.config = {
      timeout: 10000,
      cache: 'memory',
      cacheMaxAge: 5 * 60 * 1000,
      ...config,
    };

    if (this.config.cache === 'memory') {
      this.cache = new MemoryCache(this.config.cacheMaxAge);
    }
  }

  /**
   * Fetch candidate data from GraphQL
   */
  private async fetchCandidateFromGraphQL(id: string): Promise<Candidate | null> {
    const cacheKey = `graphql:candidate:${id}`;
    const cached = this.cache?.get<Candidate>(cacheKey);
    if (cached) return cached;

    try {
      const response = await this.fetchWithTimeout<Candidate>(
        this.config.graphqlEndpoint,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: `
              query getCandidateById($id: String!) {
                candidateById(id: $id) {
                  id
                  fecId
                  name
                  office
                  state
                  party
                  websiteUrl
                  email
                  phone
                  crpId
                  bioguideId
                  _labels
                  _elementId
                }
              }
            `,
            variables: { id },
          }),
        },
      );

      const candidate = response?.data?.candidateById || null;
      if (candidate) {
        this.cache?.set(cacheKey, candidate);
      }
      return candidate;
    } catch (error) {
      console.error(`Failed to fetch candidate ${id} from GraphQL:`, error);
      return null;
    }
  }

  /**
   * Fetch candidate data from Payload CMS
   */
  private async fetchCandidateFromCMS(id: string): Promise<any | null> {
    const cacheKey = `cms:candidate:${id}`;
    const cached = this.cache?.get(cacheKey);
    if (cached) return cached;

    try {
      const response = await this.fetchWithTimeout<PayloadResponse<any>>(
        `${this.config.cmsEndpoint}/candidates?where[fec_id][equals]=${encodeURIComponent(id)}`,
      );

      const doc = response?.docs?.[0] || null;
      if (doc) {
        this.cache?.set(cacheKey, doc);
      }
      return doc;
    } catch (error) {
      console.error(`Failed to fetch candidate ${id} from CMS:`, error);
      return null;
    }
  }

  /**
   * Fetch committee data from GraphQL
   */
  private async fetchCommitteeFromGraphQL(id: string): Promise<Committee | null> {
    const cacheKey = `graphql:committee:${id}`;
    const cached = this.cache?.get<Committee>(cacheKey);
    if (cached) return cached;

    try {
      const response = await this.fetchWithTimeout<Committee>(
        this.config.graphqlEndpoint,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: `
              query getCommitteeById($id: String!) {
                committeeById(id: $id) {
                  id
                  fecId
                  name
                  committeeType
                  state
                  websiteUrl
                  email
                  phone
                  _labels
                  _elementId
                }
              }
            `,
            variables: { id },
          }),
        },
      );

      const committee = response?.data?.committeeById || null;
      if (committee) {
        this.cache?.set(cacheKey, committee);
      }
      return committee;
    } catch (error) {
      console.error(`Failed to fetch committee ${id} from GraphQL:`, error);
      return null;
    }
  }

  /**
   * Fetch committee data from Payload CMS
   */
  private async fetchCommitteeFromCMS(id: string): Promise<any | null> {
    const cacheKey = `cms:committee:${id}`;
    const cached = this.cache?.get(cacheKey);
    if (cached) return cached;

    try {
      const response = await this.fetchWithTimeout<PayloadResponse<any>>(
        `${this.config.cmsEndpoint}/committees?where[fec_id][equals]=${encodeURIComponent(id)}`,
      );

      const doc = response?.docs?.[0] || null;
      if (doc) {
        this.cache?.set(cacheKey, doc);
      }
      return doc;
    } catch (error) {
      console.error(`Failed to fetch committee ${id} from CMS:`, error);
      return null;
    }
  }

  /**
   * Get merged candidate data
   */
  async getCandidate(
    id: string,
    options: MergeOptions = {},
  ): Promise<CandidateMerged | null> {
    const [graphqlData, cmsData] = await Promise.all([
      this.fetchCandidateFromGraphQL(id),
      this.fetchCandidateFromCMS(id),
    ]);

    if (!graphqlData) return null;

    // Check CMS status if onlyPublished is set
    if (options.onlyPublished && cmsData?.editorial?.status !== 'published') {
      // Return GraphQL data only
      return {
        ...graphqlData,
        _dataSource: {
          graphql: Object.keys(graphqlData),
          cms: [],
          mergedAt: new Date().toISOString(),
        },
      };
    }

    // Merge data
    const merged: CandidateMerged = {
      ...graphqlData,
      ...(cmsData && {
        cmsId: cmsData.id,
        description: cmsData.description || graphqlData.description,
        photo: cmsData.photo || undefined,
        editorial: cmsData.editorial,
      }),
    };

    // Add data source tracking if requested
    if (options.includeDataSource !== false) {
      merged._dataSource = {
        graphql: Object.keys(graphqlData),
        cms: cmsData ? Object.keys(cmsData).filter((k) => !k.startsWith('_')) : [],
        mergedAt: new Date().toISOString(),
      };
    }

    return merged;
  }

  /**
   * Get merged committee data
   */
  async getCommittee(
    id: string,
    options: MergeOptions = {},
  ): Promise<CommitteeMerged | null> {
    const [graphqlData, cmsData] = await Promise.all([
      this.fetchCommitteeFromGraphQL(id),
      this.fetchCommitteeFromCMS(id),
    ]);

    if (!graphqlData) return null;

    // Check CMS status if onlyPublished is set
    if (options.onlyPublished && cmsData?.editorial?.status !== 'published') {
      return {
        ...graphqlData,
        _dataSource: {
          graphql: Object.keys(graphqlData),
          cms: [],
          mergedAt: new Date().toISOString(),
        },
      };
    }

    // Merge data
    const merged: CommitteeMerged = {
      ...graphqlData,
      ...(cmsData && {
        cmsId: cmsData.id,
        description: cmsData.description || graphqlData.description,
        logo: cmsData.logo || undefined,
        editorial: cmsData.editorial,
      }),
    };

    // Add data source tracking if requested
    if (options.includeDataSource !== false) {
      merged._dataSource = {
        graphql: Object.keys(graphqlData),
        cms: cmsData ? Object.keys(cmsData).filter((k) => !k.startsWith('_')) : [],
        mergedAt: new Date().toISOString(),
      };
    }

    return merged;
  }

  /**
   * Get merged individual data
   */
  async getIndividual(
    id: string,
    options: MergeOptions = {},
  ): Promise<IndividualMerged | null> {
    const cacheKey = `graphql:individual:${id}`;
    const cached = this.cache?.get<Individual>(cacheKey);
    const graphqlData = cached || (await this.fetchIndividualFromGraphQL(id));

    if (!graphqlData) return null;

    const cmsCacheKey = `cms:individual:${id}`;
    const cmsCached = this.cache?.get(cmsCacheKey);
    const cmsData = cmsCached || (await this.fetchIndividualFromCMS(id));

    // Merge data
    const merged: IndividualMerged = {
      ...graphqlData,
      ...(cmsData && {
        cmsId: cmsData.id,
        biography: cmsData.biography || undefined,
        photo: cmsData.photo || undefined,
        editorial: cmsData.editorial,
      }),
    };

    // Add data source tracking if requested
    if (options.includeDataSource !== false) {
      merged._dataSource = {
        graphql: Object.keys(graphqlData),
        cms: cmsData ? Object.keys(cmsData).filter((k) => !k.startsWith('_')) : [],
        mergedAt: new Date().toISOString(),
      };
    }

    return merged;
  }

  /**
   * Fetch individual from GraphQL (private)
   */
  private async fetchIndividualFromGraphQL(id: string): Promise<Individual | null> {
    try {
      const response = await this.fetchWithTimeout<Individual>(
        this.config.graphqlEndpoint,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: `
              query getIndividualById($id: String!) {
                individualById(id: $id) {
                  id
                  name
                  city
                  state
                  zip
                  occupation
                  employer
                  _labels
                  _elementId
                }
              }
            `,
            variables: { id },
          }),
        },
      );

      return response?.data?.individualById || null;
    } catch (error) {
      console.error(`Failed to fetch individual ${id} from GraphQL:`, error);
      return null;
    }
  }

  /**
   * Fetch individual from CMS (private)
   */
  private async fetchIndividualFromCMS(id: string): Promise<any | null> {
    try {
      const response = await this.fetchWithTimeout<PayloadResponse<any>>(
        `${this.config.cmsEndpoint}/individuals?where[neo4j_id][equals]=${encodeURIComponent(id)}`,
      );

      return response?.docs?.[0] || null;
    } catch (error) {
      console.error(`Failed to fetch individual ${id} from CMS:`, error);
      return null;
    }
  }

  /**
   * Helper to fetch with timeout
   */
  private async fetchWithTimeout<T>(
    url: string,
    options?: RequestInit,
  ): Promise<T> {
    const controller = new AbortController();
    const timeoutId = setTimeout(
      () => controller.abort(),
      this.config.timeout || 10000,
    );

    try {
      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } finally {
      clearTimeout(timeoutId);
    }
  }

  /**
   * Clear cache
   */
  clearCache(): void {
    this.cache?.clear();
  }
}

/**
 * Factory function for creating CMS loader with sensible defaults
 */
export function createCMSLoader(
  graphqlEndpoint: string,
  cmsEndpoint: string,
  options?: Partial<CMSLoaderConfig>,
): CMSLoader {
  return new CMSLoader({
    graphqlEndpoint,
    cmsEndpoint,
    ...options,
  });
}
