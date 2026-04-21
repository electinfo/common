/**
 * Entity type definitions matching Neo4j GraphQL API responses
 * Source of truth for all entity data across elect.info
 */

// ============================================================================
// POLITICIANS
// ============================================================================

/**
 * Politician - Federal election candidate and office holder
 * Matches Neo4j :Politician node and GraphQL Query.politicians response
 */
export interface Politician {
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
// CODE SOURCES (CMS-native)
// ============================================================================

/**
 * CodeSource - Open source code repository powering elect.info
 * CMS-native entity: Payload CMS is the authoritative source (not Neo4j)
 */
export interface CodeSource {
  id: string; // Payload document ID
  name: string;
  url: string;
  domain: string;
  description?: string;
  repos: string[];

  // Editorial
  cmsStatus: 'draft' | 'published' | 'archived';
  cmsNotes?: string;

  // Payload timestamps
  createdAt?: string;
  updatedAt?: string;
}

// ============================================================================
// DATA SOURCES (CMS-native)
// ============================================================================

/**
 * Canonical data type categories available from data sources.
 * Values match Payload CMS select options on the DataSource collection.
 */
export enum DataType {
  ACTIONS = 'actions',
  BALLOT_MEASURES = 'ballot-measures',
  BILLS = 'bills',
  CAMPAIGN_FINANCE = 'campaign-finance',
  CANDIDATES = 'candidates',
  COMMITTEES = 'committees',
  CONGRESSIONAL_DISTRICTS = 'congressional-districts',
  CONGRESSIONAL_RECORD = 'congressional-record',
  CONTACT_INFORMATION = 'contact-information',
  CONTRIBUTIONS = 'contributions',
  CORPORATE_OWNERSHIP = 'corporate-ownership',
  COUNTIES = 'counties',
  COUNTY_RESULTS = 'county-results',
  DEMOGRAPHICS = 'demographics',
  ELECTION_RESULTS = 'election-results',
  EVENTS = 'events',
  EXPENDITURES = 'expenditures',
  FILINGS = 'filings',
  GLOBAL_KNOWLEDGE_GRAPH = 'global-knowledge-graph',
  JURISDICTIONS = 'jurisdictions',
  LEGAL_ENTITIES = 'legal-entities',
  LEGISLATORS = 'legislators',
  LOBBYING = 'lobbying',
  MEMBERS = 'members',
  NEWS_ARTICLES = 'news-articles',
  ORGANIZATIONS = 'organizations',
  PARENT_SUBSIDIARY_RELATIONSHIPS = 'parent-subsidiary-relationships',
  PEOPLE = 'people',
  PLACES = 'places',
  PRECINCT_BOUNDARIES = 'precinct-boundaries',
  PRECINCT_RESULTS = 'precinct-results',
  RESOLUTIONS = 'resolutions',
  SESSIONS = 'sessions',
  SPONSORS = 'sponsors',
  STATE_DISTRICTS = 'state-districts',
  STATES = 'states',
  VOTE_COUNTS = 'vote-counts',
  VOTER_DEMOGRAPHICS = 'voter-demographics',
  VOTER_REGISTRATION = 'voter-registration',
  VOTES = 'votes',
  ZIP_CODES = 'zip-codes',
}

/**
 * Human-readable labels for DataType enum values
 */
export const DataTypeLabels: Record<DataType, string> = {
  [DataType.ACTIONS]: 'Actions',
  [DataType.BALLOT_MEASURES]: 'Ballot Measures',
  [DataType.BILLS]: 'Bills',
  [DataType.CAMPAIGN_FINANCE]: 'Campaign Finance',
  [DataType.CANDIDATES]: 'Candidates',
  [DataType.COMMITTEES]: 'Committees',
  [DataType.CONGRESSIONAL_DISTRICTS]: 'Congressional Districts',
  [DataType.CONGRESSIONAL_RECORD]: 'Congressional Record',
  [DataType.CONTACT_INFORMATION]: 'Contact Information',
  [DataType.CONTRIBUTIONS]: 'Contributions',
  [DataType.CORPORATE_OWNERSHIP]: 'Corporate Ownership',
  [DataType.COUNTIES]: 'Counties',
  [DataType.COUNTY_RESULTS]: 'County Results',
  [DataType.DEMOGRAPHICS]: 'Demographics',
  [DataType.ELECTION_RESULTS]: 'Election Results',
  [DataType.EVENTS]: 'Events',
  [DataType.EXPENDITURES]: 'Expenditures',
  [DataType.FILINGS]: 'Filings',
  [DataType.GLOBAL_KNOWLEDGE_GRAPH]: 'Global Knowledge Graph',
  [DataType.JURISDICTIONS]: 'Jurisdictions',
  [DataType.LEGAL_ENTITIES]: 'Legal Entities',
  [DataType.LEGISLATORS]: 'Legislators',
  [DataType.LOBBYING]: 'Lobbying',
  [DataType.MEMBERS]: 'Members',
  [DataType.NEWS_ARTICLES]: 'News Articles',
  [DataType.ORGANIZATIONS]: 'Organizations',
  [DataType.PARENT_SUBSIDIARY_RELATIONSHIPS]: 'Parent-Subsidiary Relationships',
  [DataType.PEOPLE]: 'People',
  [DataType.PLACES]: 'Places',
  [DataType.PRECINCT_BOUNDARIES]: 'Precinct Boundaries',
  [DataType.PRECINCT_RESULTS]: 'Precinct Results',
  [DataType.RESOLUTIONS]: 'Resolutions',
  [DataType.SESSIONS]: 'Sessions',
  [DataType.SPONSORS]: 'Sponsors',
  [DataType.STATE_DISTRICTS]: 'State Districts',
  [DataType.STATES]: 'States',
  [DataType.VOTE_COUNTS]: 'Vote Counts',
  [DataType.VOTER_DEMOGRAPHICS]: 'Voter Demographics',
  [DataType.VOTER_REGISTRATION]: 'Voter Registration',
  [DataType.VOTES]: 'Votes',
  [DataType.ZIP_CODES]: 'ZIP Codes',
};

/**
 * DataSource - External data source powering elect.info
 * CMS-native entity: Payload CMS is the authoritative source (not Neo4j)
 */
export interface DataSource {
  id: string; // Payload document ID
  name: string;
  url: string;
  domain: string;
  description: string;
  dataTypes: DataType[];
  icon?: string; // Emoji icon for display

  // Editorial
  cmsStatus: 'draft' | 'published' | 'archived';
  cmsNotes?: string;

  // Payload timestamps
  createdAt?: string;
  updatedAt?: string;
}

// ============================================================================
// UNION TYPES & HELPERS
// ============================================================================

/**
 * Any entity type that can have a description in the CMS
 */
export type CmsEntity = Politician | CodeSource | Committee | DataSource | Individual;

/**
 * All entity types
 */
export type AnyEntity =
  | Politician
  | CodeSource
  | Committee
  | DataSource
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
  POLITICIAN = 'politician',
  CODE_SOURCE = 'code-source',
  COMMITTEE = 'committee',
  DATA_SOURCE = 'data-source',
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
 * Type guard to check if entity is a Politician
 */
export function isPolitician(entity: any): entity is Politician {
  return entity && 'office' in entity && ['president', 'senate', 'house'].includes(entity.office);
}

/**
 * Type guard to check if entity is a CodeSource
 */
export function isCodeSource(entity: any): entity is CodeSource {
  return entity && 'domain' in entity && 'repos' in entity && Array.isArray(entity.repos);
}

/**
 * Type guard to check if entity is a Committee
 */
export function isCommittee(entity: any): entity is Committee {
  return entity && 'type' in entity && ['pac', 'super-pac', 'party', 'hybrid', 'leadership', 'other'].includes(entity.type);
}

/**
 * Type guard to check if entity is a DataSource
 */
export function isDataSource(entity: any): entity is DataSource {
  return entity && 'domain' in entity && 'dataTypes' in entity && Array.isArray(entity.dataTypes);
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
  if (isPolitician(entity)) return EntityType.POLITICIAN;
  if (isCodeSource(entity)) return EntityType.CODE_SOURCE;
  if (isCommittee(entity)) return EntityType.COMMITTEE;
  if (isDataSource(entity)) return EntityType.DATA_SOURCE;
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
