/**
 * CMS-Merged Entity Types
 *
 * These types represent entities enriched with CMS editorial content.
 * They combine data from:
 * - Neo4j GraphQL (authoritative source)
 * - Payload CMS (editorial enrichment)
 */

import type { Candidate, Committee, Individual } from './entities';

/**
 * CMS Candidate: Extends Neo4j Candidate with editorial enrichment
 */
export interface CandidateMerged extends Candidate {
  // CMS Editorial Fields
  cmsId?: string; // Payload document ID
  description?: string; // Rich text biography/description
  photo?: {
    url: string;
    alt?: string;
    caption?: string;
  };
  // Editorial Metadata
  editorial?: {
    status: 'draft' | 'published' | 'archived';
    lastCuratedBy?: string;
    lastCuratedAt?: string;
    verifiedAt?: string;
    internalNotes?: string;
  };
  // Data Source Tracking
  _dataSource?: {
    graphql: string[]; // Fields from Neo4j
    cms: string[]; // Fields from Payload
    mergedAt: string;
  };
}

/**
 * CMS Committee: Extends Neo4j Committee with editorial enrichment
 */
export interface CommitteeMerged extends Committee {
  // CMS Editorial Fields
  cmsId?: string;
  description?: string;
  logo?: {
    url: string;
    alt?: string;
  };
  // Editorial Metadata
  editorial?: {
    status: 'draft' | 'published' | 'archived';
    lastCuratedBy?: string;
    lastCuratedAt?: string;
    verifiedAt?: string;
    internalNotes?: string;
  };
  // Data Source Tracking
  _dataSource?: {
    graphql: string[];
    cms: string[];
    mergedAt: string;
  };
}

/**
 * CMS Individual: Extends Neo4j Individual with editorial enrichment
 */
export interface IndividualMerged extends Individual {
  // CMS Editorial Fields
  cmsId?: string;
  biography?: string;
  photo?: {
    url: string;
    alt?: string;
  };
  // Editorial Metadata
  editorial?: {
    status: 'draft' | 'published' | 'archived';
    lastCuratedBy?: string;
    lastCuratedAt?: string;
    verifiedAt?: string;
    internalNotes?: string;
  };
  // Data Source Tracking
  _dataSource?: {
    graphql: string[];
    cms: string[];
    mergedAt: string;
  };
}

/**
 * Type guard for CandidateMerged
 */
export function isCandidateMerged(entity: unknown): entity is CandidateMerged {
  return (
    typeof entity === 'object' &&
    entity !== null &&
    'id' in entity &&
    'fecId' in entity &&
    'name' in entity &&
    'office' in entity
  );
}

/**
 * Type guard for CommitteeMerged
 */
export function isCommitteeMerged(entity: unknown): entity is CommitteeMerged {
  return (
    typeof entity === 'object' &&
    entity !== null &&
    'id' in entity &&
    'fecId' in entity &&
    'name' in entity &&
    'committeeType' in entity
  );
}

/**
 * Type guard for IndividualMerged
 */
export function isIndividualMerged(entity: unknown): entity is IndividualMerged {
  return (
    typeof entity === 'object' &&
    entity !== null &&
    'id' in entity &&
    'name' in entity &&
    'city' in entity &&
    'state' in entity
  );
}
