#!/usr/bin/env node
/**
 * Convert all YAML files in schemas/ to JSON for TypeScript consumption.
 * Source of truth is the YAML; JSON files are gitignored.
 */
const yaml = require('js-yaml');
const fs = require('fs');
const path = require('path');

const schemasDir = path.join(__dirname, '..', 'schemas');

fs.readdirSync(schemasDir)
  .filter(f => f.endsWith('.yaml'))
  .forEach(yamlFile => {
    const yamlPath = path.join(schemasDir, yamlFile);
    const jsonFile = yamlFile.replace('.yaml', '.json');
    const jsonPath = path.join(schemasDir, jsonFile);
    const data = yaml.load(fs.readFileSync(yamlPath, 'utf8'));
    fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2) + '\n');
  });
