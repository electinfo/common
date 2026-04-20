// AUTO-GENERATED from schemas/quicksilver-metamodel.json — DO NOT EDIT
// Regenerate with: npm run generate:scala
package info.elect.model

import org.apache.spark.sql.types.{DataType, StructType}
import info.elect.model.entities.CandidateEntity
import info.elect.model.entities.CommitteeEntity
import info.elect.model.entities.IndividualEntity
import info.elect.model.entities.VendorEntity
import info.elect.model.entities.EmployerEntity
import info.elect.model.entities.CompanyEntity
import info.elect.model.entities.OfficeEntity
import info.elect.model.entities.CycleEntity
import info.elect.model.entities.PartyEntity
import info.elect.model.entities.OfficeCandidateStats
import info.elect.model.entities.OfficeholderEntity
import info.elect.model.entities.RaceEntity
import info.elect.model.entities.VoterEntity
import info.elect.model.entities.StateEntity
import info.elect.model.entities.CountyEntity
import info.elect.model.entities.DistrictEntity
import info.elect.model.entities.PlaceEntity
import info.elect.model.entities.PostalcodeEntity
import info.elect.model.entities.TractEntity
import info.elect.model.entities.BlockEntity
import info.elect.model.entities.PrecinctEntity
import info.elect.model.entities.CatalogMetaEntity
import info.elect.model.entities.TableMetaEntity
import info.elect.model.entities.FieldMetaEntity
import info.elect.model.entities.SourceIdEntity
import info.elect.model.entities.CandidateNameVertex
import info.elect.model.entities.CommitteeNameVertex
import info.elect.model.edges.CandidateStateEdge
import info.elect.model.edges.CandidatePlaceEdge
import info.elect.model.edges.CandidateZipEdge
import info.elect.model.edges.CandidateCountyEdge
import info.elect.model.edges.CandidateDistrictEdge
import info.elect.model.edges.CandidateOfficeholderEdge
import info.elect.model.edges.CandidateSourceIdEdge
import info.elect.model.edges.CandidateNameEdge
import info.elect.model.edges.CommitteeNameEdge
import info.elect.model.edges.IndividualCommitteeEdge
import info.elect.model.edges.CommitteeVendorEdge
import info.elect.model.edges.CommitteeCandidateEdge
import info.elect.model.edges.CommitteeCommitteeEdge
import info.elect.model.edges.IndividualEmployerEdge
import info.elect.model.edges.IndividualPlaceEdge
import info.elect.model.edges.IndividualPostalcodeEdge
import info.elect.model.edges.CandidatePartyEdge
import info.elect.model.edges.CandidateCycleEdge
import info.elect.model.edges.CandidateOfficeEdge
import info.elect.model.edges.CommitteeCycleEdge
import info.elect.model.edges.OfficeholderDistrictEdge
import info.elect.model.edges.OfficeholderStateEdge
import info.elect.model.edges.OfficeholderRaceEdge
import info.elect.model.edges.OfficeholderOfficeEdge
import info.elect.model.edges.CandidateRaceEdge
import info.elect.model.edges.RaceOfficeEdge
import info.elect.model.edges.RaceStateEdge
import info.elect.model.edges.RaceCycleEdge
import info.elect.model.edges.CountyStateEdge
import info.elect.model.edges.DistrictStateEdge
import info.elect.model.edges.DistrictCountyEdge
import info.elect.model.edges.DistrictPlaceEdge
import info.elect.model.edges.TractStateEdge
import info.elect.model.edges.TractCountyEdge
import info.elect.model.edges.TractDistrictEdge
import info.elect.model.edges.PlaceStateEdge
import info.elect.model.edges.PostalcodeDistrictEdge
import info.elect.model.edges.DatasourceCatalogEdge
import info.elect.model.edges.CatalogTableEdge
import info.elect.model.edges.TableFieldEdge

/**
 * Schema registry and utilities.
 * Individual schemas live in info.elect.model.entities.* and info.elect.model.edges.*.
 * This object provides the consolidated registry for lookup and validation.
 */
object QuicksilverSchemas extends SchemaBase {

  val registry: Map[String, StructType] = Map(
    "candidate_entities" -> CandidateEntity.schema,
    "committee_entities" -> CommitteeEntity.schema,
    "individual_entities" -> IndividualEntity.schema,
    "vendor_entities" -> VendorEntity.schema,
    "employer_entities" -> EmployerEntity.schema,
    "company_entities" -> CompanyEntity.schema,
    "office_entities" -> OfficeEntity.schema,
    "office_candidate_stats" -> OfficeCandidateStats.schema,
    "party_entities" -> PartyEntity.schema,
    "cycle_entities" -> CycleEntity.schema,
    "officeholder_entities" -> OfficeholderEntity.schema,
    "race_entities" -> RaceEntity.schema,
    "state_entities" -> StateEntity.schema,
    "county_entities" -> CountyEntity.schema,
    "district_entities" -> DistrictEntity.schema,
    "place_entities" -> PlaceEntity.schema,
    "postalcode_entities" -> PostalcodeEntity.schema,
    "tract_entities" -> TractEntity.schema,
    "block_entities" -> BlockEntity.schema,
    "precinct_entities" -> PrecinctEntity.schema,
    "source_id_entities" -> SourceIdEntity.schema,
    "candidate_name_vertices" -> CandidateNameVertex.schema,
    "committee_name_vertices" -> CommitteeNameVertex.schema,
    "candidate_state_edges" -> CandidateStateEdge.schema,
    "candidate_place_edges" -> CandidatePlaceEdge.schema,
    "candidate_zip_edges" -> CandidateZipEdge.schema,
    "candidate_county_edges" -> CandidateCountyEdge.schema,
    "candidate_district_edges" -> CandidateDistrictEdge.schema,
    "candidate_officeholder_edges" -> CandidateOfficeholderEdge.schema,
    "candidate_source_id_edges" -> CandidateSourceIdEdge.schema,
    "candidate_name_edges" -> CandidateNameEdge.schema,
    "committee_name_edges" -> CommitteeNameEdge.schema,
    "individual_committee_edges" -> IndividualCommitteeEdge.schema,
    "individual_employer_edges" -> IndividualEmployerEdge.schema,
    "individual_place_edges" -> IndividualPlaceEdge.schema,
    "individual_postalcode_edges" -> IndividualPostalcodeEdge.schema,
    "committee_committee_edges" -> CommitteeCommitteeEdge.schema,
    "committee_vendor_edges" -> CommitteeVendorEdge.schema,
    "committee_candidate_edges" -> CommitteeCandidateEdge.schema,
    "candidate_party_edges" -> CandidatePartyEdge.schema,
    "candidate_cycle_edges" -> CandidateCycleEdge.schema,
    "candidate_office_edges" -> CandidateOfficeEdge.schema,
    "committee_cycle_edges" -> CommitteeCycleEdge.schema,
    "officeholder_district_edges" -> OfficeholderDistrictEdge.schema,
    "officeholder_state_edges" -> OfficeholderStateEdge.schema,
    "officeholder_race_edges" -> OfficeholderRaceEdge.schema,
    "officeholder_office_edges" -> OfficeholderOfficeEdge.schema,
    "candidate_race_edges" -> CandidateRaceEdge.schema,
    "race_office_edges" -> RaceOfficeEdge.schema,
    "race_state_edges" -> RaceStateEdge.schema,
    "race_cycle_edges" -> RaceCycleEdge.schema,
    "county_state_edges" -> CountyStateEdge.schema,
    "district_state_edges" -> DistrictStateEdge.schema,
    "district_county_edges" -> DistrictCountyEdge.schema,
    "district_place_edges" -> DistrictPlaceEdge.schema,
    "tract_state_edges" -> TractStateEdge.schema,
    "tract_county_edges" -> TractCountyEdge.schema,
    "tract_district_edges" -> TractDistrictEdge.schema,
    "place_state_edges" -> PlaceStateEdge.schema,
    "postalcode_district_edges" -> PostalcodeDistrictEdge.schema,
    "voter_entities" -> VoterEntity.schema,
    "catalog_meta_entities" -> CatalogMetaEntity.schema,
    "table_meta_entities" -> TableMetaEntity.schema,
    "field_meta_entities" -> FieldMetaEntity.schema,
    "datasource_catalog_edges" -> DatasourceCatalogEdge.schema,
    "catalog_table_edges" -> CatalogTableEdge.schema,
    "table_field_edges" -> TableFieldEdge.schema
  )

  /** Extract required column names from a canonical schema. */
  def requiredColumns(schema: StructType): Set[String] =
    schema.fields.filter(!_.nullable).map(_.name).toSet

  /** Extract all column names from a canonical schema. */
  def allColumns(schema: StructType): Set[String] =
    schema.fields.map(_.name).toSet

  /** Build a column name -> DataType map for a canonical schema. */
  def columnTypes(schema: StructType): Map[String, DataType] =
    schema.fields.map(f => f.name -> f.dataType).toMap

  /**
   * Resolve a table name to its canonical schema.
   * First tries exact match, then civitech per-state pattern.
   */
  def resolve(tableName: String): Option[StructType] = {
    registry.get(tableName).orElse {
      val civitechPattern = """^civitech_com_voter_[a-z]{2}_(.+)$""".r
      tableName match {
        case civitechPattern(suffix) =>
          val baseName = suffix match {
            case "entities" => "voter_entities"
            case _ => None.orNull
          }
          if (baseName != null) registry.get(baseName) else None
        case _ => None
      }
    }
  }
}
