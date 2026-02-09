/**
 * @electinfo/common - Shared schemas and constants
 */

import urlPatterns from '../../../schemas/url-patterns.json';
import constants from '../../../schemas/constants.json';
import entityTypesSchema from '../../../schemas/entity-types.json';

// Re-export raw schemas
export { urlPatterns, constants, entityTypesSchema };

// Type definitions
export interface UrlPatternConfig {
  candidate: {
    president: (slug: string) => string;
    senate: (state: string, slug: string) => string;
    house: (state: string, district: string, slug: string) => string;
  };
  committee: (type: string, slug: string, id: string) => string;
  individual: (slug: string, id: string) => string;
  employer: (slug: string, id: string) => string;
  vendor: (slug: string, id: string) => string;
  party: (slug: string) => string;
  district: (slug: string) => string;
  state: (slug: string) => string;
  cycle: (year: string | number) => string;
}

// URL pattern generators
export const UrlPatterns: UrlPatternConfig = {
  candidate: {
    president: (slug: string) => `/candidates/president/us/${slug}/`,
    senate: (state: string, slug: string) => `/candidates/senate/${state.toLowerCase()}/${slug}/`,
    house: (state: string, district: string, slug: string) => {
      const districtPadded = district.toString().padStart(2, '0');
      return `/candidates/house/${state.toLowerCase()}-${districtPadded}/${slug}/`;
    }
  },
  committee: (type: string, slug: string, id: string) => `/committees/${type}/${slug}-${id.toLowerCase()}/`,
  individual: (slug: string, id: string) => {
    const idClean = id.replace(/^I-/i, '').toLowerCase();
    const idSuffix = idClean.slice(0, 12);
    return `/individuals/${slug}-i-${idSuffix}/`;
  },
  employer: (slug: string, id: string) => {
    const idClean = id.replace(/^O-/i, '').toLowerCase();
    return `/employers/${slug}-${idClean}/`;
  },
  vendor: (slug: string, id: string) => {
    const idClean = id.replace(/^V-/i, '').toLowerCase();
    return `/vendors/${slug}-${idClean}/`;
  },
  party: (slug: string) => `/parties/${slug}/`,
  district: (slug: string) => `/districts/${slug}/`,
  state: (slug: string) => `/states/${slug}/`,
  cycle: (year: string | number) => `/elections/${year}/`
};

// Constants with proper typing
export const Constants = {
  stateNames: constants.stateNames as Record<string, string>,
  partyNames: constants.partyNames as Record<string, string>,
  officeNames: constants.officeNames as Record<string, string>,
  committeeTypeSlugs: constants.committeeTypeSlugs as Record<string, string>,
  committeeTypeNames: constants.committeeTypeNames as Record<string, string>,
  incumbentStatus: constants.incumbentStatus as Record<string, string>
};

// Slug generation (matches Python/Scala implementations)
export function makeSlug(name: string): string {
  if (!name) return '';
  return name
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

// Entity type registry
const entityTypes = entityTypesSchema.entityTypes as Record<string, { plural: string }>;

/**
 * Returns the canonical path for an entity: {plural}/{id.toLowerCase()}
 */
export function canonicalPath(entityType: string, id: string): string {
  const config = entityTypes[entityType];
  if (!config) {
    throw new Error(`Unknown entity type: ${entityType}`);
  }
  return `${config.plural}/${id.toLowerCase()}`;
}