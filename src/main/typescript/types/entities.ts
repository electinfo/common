/**
 * Entity type definitions matching Neo4j GraphQL API responses
 * Source of truth for all entity data across elect.info
 */

// ============================================================================
// CANDIDATES
// ============================================================================

/**
 * Candidate - Federal election candidate
 * Matches Neo4j :Candidate node and GraphQL Query.candidates response
 */
export interface Candidate {
  // Core identifiers
  id: string; // Neo4j node ID
  fecId: string; // FEC candidate ID (unique)

  // Basic info
  name: string;
  office: 'president' | 'senate' | 'house';
  state?: string;
  district?: string;

  // Politics
  party: 'democratic' | 'republican' | 'independent' | 'libertarian' | 'green' | 'other';
  partyAffiliation?: string;

  // Contact & web
  websiteUrl?: string;
  email?: string;
  phone?: string;

  // External IDs
  crpId?: string; // Center for Responsive Politics ID
  bioguideId?: string; // Congressional Bioguide ID

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// COMMITTEES
// ============================================================================

/**
 * Committee - Political Action Committee or other fundraising committee
 * Matches Neo4j :Committee node and GraphQL Query.committees response
 */
export interface Committee {
  // Core identifiers
  id: string; // Neo4j node ID
  fecId: string; // FEC committee ID (unique)

  // Basic info
  name: string;
  type: 'pac' | 'super-pac' | 'party' | 'hybrid' | 'leadership' | 'other';
  state?: string;

  // Leadership
  treasurer?: string;
  treasurerPhone?: string;
  treasurerEmail?: string;

  // Classification
  designationCode?: string; // 'A' (Authorized), 'B' (Ballot), 'U' (Unauthorized), etc.

  // External IDs
  crpId?: string; // Center for Responsive Politics ID

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// INDIVIDUALS / DONORS
// ============================================================================

/**
 * Individual - Person who has made campaign contributions
 * Matches Neo4j :Individual node and GraphQL Query.individuals response
 */
export interface Individual {
  // Core identifiers
  id: string; // Neo4j node ID
  name: string;

  // Location
  address?: string;
  city?: string;
  state?: string;
  zip?: string;

  // Work
  employer?: string;
  occupation?: string;

  // Classification
  entityType: 'individual';

  // Aggregates
  totalContributions?: number;
  numberOfContributions?: number;

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

/**
 * Donor - Alias for Individual (used in donor context)
 */
export type Donor = Individual;

// ============================================================================
// OFFICES
// ============================================================================

/**
 * Office - Political office (President, Senate seat, House seat, etc.)
 * Matches Neo4j :Office node
 */
export interface Office {
  id: string;
  type: 'president' | 'senate' | 'house' | 'governor' | 'other';
  name: string;
  state?: string; // Two-letter state code (null for President)
  district?: string; // House district number
  class?: string; // Senate class (1, 2, or 3)

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// DISTRICTS
// ============================================================================

/**
 * District - Congressional or electoral district
 * Matches Neo4j :District node
 */
export interface District {
  id: string;
  name: string;
  state: string; // Two-letter state code
  number: number; // District number

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// STATES
// ============================================================================

/**
 * State - US state or territory
 * Matches Neo4j :State node
 */
export interface State {
  id: string;
  name: string;
  code: string; // Two-letter state code
  fips?: string; // FIPS code
  population?: number;

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// PARTIES
// ============================================================================

/**
 * Party - Political party
 * Matches Neo4j :Party node
 */
export interface Party {
  id: string;
  name: string;
  code: string; // Short code (D, R, I, G, L, etc.)
  abbreviation?: string;

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// CONTRIBUTIONS & TRANSACTIONS
// ============================================================================

/**
 * Contribution - Single contribution from a donor to a candidate/committee
 * Matches Neo4j :Contribution relationship
 */
export interface Contribution {
  id: string;
  amount: number;
  date: string; // ISO 8601 date
  recipientId: string; // Candidate or Committee FEC ID
  donorId: string; // Individual FEC ID or Committee FEC ID
  donorName: string;
  donorType: 'individual' | 'committee';
  purpose?: string;
  transactionId?: string; // FEC transaction ID

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// ELECTIONS & CYCLES
// ============================================================================

/**
 * Election - Federal election cycle
 * Matches Neo4j :Election node
 */
export interface Election {
  id: string;
  year: number;
  type: 'general' | 'primary' | 'special' | 'runoff';
  date: string; // ISO 8601 date
  offices: string[]; // Office IDs that had races in this election

  // Neo4j metadata (optional)
  _labels?: string[];
  _elementId?: string;
}

// ============================================================================
// UNION TYPES & HELPERS
// ============================================================================

/**
 * Any entity type that can have a description in the CMS
 */
export type CmsEntity = Candidate | Committee | Individual;

/**
 * All entity types
 */
export type AnyEntity =
  | Candidate
  | Committee
  | Individual
  | Office
  | District
  | State
  | Party
  | Election
  | Contribution;

/**
 * Entity type enumeration
 */
export enum EntityType {
  CANDIDATE = 'candidate',
  COMMITTEE = 'committee',
  INDIVIDUAL = 'individual',
  DONOR = 'donor', // Alias for individual
  OFFICE = 'office',
  DISTRICT = 'district',
  STATE = 'state',
  PARTY = 'party',
  ELECTION = 'election',
  CONTRIBUTION = 'contribution'
}

/**
 * Type guard to check if entity is a Candidate
 */
export function isCandidate(entity: any): entity is Candidate {
  return entity && 'office' in entity && ['president', 'senate', 'house'].includes(entity.office);
}

/**
 * Type guard to check if entity is a Committee
 */
export function isCommittee(entity: any): entity is Committee {
  return entity && 'type' in entity && ['pac', 'super-pac', 'party', 'hybrid', 'leadership', 'other'].includes(entity.type);
}

/**
 * Type guard to check if entity is an Individual
 */
export function isIndividual(entity: any): entity is Individual {
  return entity && entity.entityType === 'individual';
}

/**
 * Get entity type from an entity object
 */
export function getEntityType(entity: any): EntityType | null {
  if (isCandidate(entity)) return EntityType.CANDIDATE;
  if (isCommittee(entity)) return EntityType.COMMITTEE;
  if (isIndividual(entity)) return EntityType.INDIVIDUAL;
  if (entity && entity.type === 'office') return EntityType.OFFICE;
  if (entity && 'number' in entity && entity.state) return EntityType.DISTRICT;
  if (entity && 'code' in entity && entity.code?.length === 2) return EntityType.STATE;
  if (entity && 'abbreviation' in entity) return EntityType.PARTY;
  if (entity && 'year' in entity) return EntityType.ELECTION;
  return null;
}

/**
 * Interface for paginated GraphQL responses
 */
export interface PaginatedResponse<T> {
  docs: T[];
  totalDocs: number;
  limit: number;
  page: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPrevPage: boolean;
  nextPage?: number;
  prevPage?: number;
}

/**
 * GraphQL query result wrapper
 */
export interface GraphQLResponse<T> {
  data?: {
    [key: string]: T | T[] | PaginatedResponse<T>;
  };
  errors?: Array<{
    message: string;
    extensions?: Record<string, any>;
  }>;
}
