# Concept Validation

## Steps

1. We will create a Python program that validates a simple flat Concepts file.
2. We will validate the file with a JSON schema file
3. We will then be able to validate that a Concepts file has the three required fields
4. We will then show how additional fields can be added to make the glossary into a full taxonomy

## JSON Schema File

This schema file definds the fields and creates a defintion for each field.

The following fields are REQUIRED fields.

1. conceptID
2. prefLabel
3. definition

The following fields are optional

1. altLabel
2. notes

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Business Glossary for Financial Fraud Analysis",
    "description": "A schema for validating entries in a business glossary related to financial fraud analysis.",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "conceptID": {
                "type": "string",
                "description": "A unique identifier for the concept."
            },
            "prefLabel": {
                "type": "string",
                "description": "The preferred label of the concept."
            },
            "altLabels": {
                "type": "array",
                "description": "A list of alternative labels for the concept.",
                "items": {
                    "type": "string"
                }
            },
            "definition": {
                "type": "string",
                "description": "A clear and concise definition of the concept."
            },
            "notes": {
                "type": "string",
                "description": "Additional notes regarding the concept."
            }
        },
        "required": ["conceptID", "prefLabel", "definition"],
        "additionalProperties": false
    }
}

```

### Create a Conda Environment With Required Libraries

We will need two libraries:

1. jsonschema
2. argparse

```sh
conda create -n "concepts" python=3
conda activate python
pip install jsonschema argparse
```

### Running the Validate Command from the Command Line Shell

Our validation program takes two arguments:

1. The first file is the file to validate.
2. The second file is the schema file.

Example:

```sh
python validate-concepts.py my-glossary.json concept-schema.json
```

Sample Response:
```
JSON data is valid.
```

## Taxonomy Structure

We now add a few more fields to the simple flat-file of concents.

1. All taxonomy elements are in a scheme
2. A scheme has one and only-one top-level element
3. Every concept can have zero or more narrower concepts

Sample Schema for Validating a Taxonomy JSON file:

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Taxonomy Schema Concept File ",
    "description": "A schema for validating entries in a taxonomy of concepts in a scheme.",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "conceptID": {
                "type": "string",
                "description": "A unique identifier for the concept."
            },
            "prefLabel": {
                "type": "string",
                "description": "The preferred label of the concept."
            },
            "altLabels": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "A list of alternative labels for the concept."
            },
            "definition": {
                "type": "string",
                "description": "A clear and concise definition of the concept."
            },
            "notes": {
                "type": "string",
                "description": "Additional notes regarding the concept."
            },
            "inScheme": {
                "type": "string",
                "description": "The name of the scheme the concept is part of."
            },
            "topConceptOf": {
                "type": "boolean",
                "description": "Indicates if the concept is the top concept of a scheme."
            },
            "narrower": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "List of conceptIDs that are narrower concepts of this concept."
            }
        },
        "required": ["conceptID", "prefLabel", "definition"],
        "additionalProperties": false
    }
}

```

Sample Taxonomy file for Products:

[Sample Food Taxonomy](https://github.com/dmccrearytg/c360/blob/main/data/concepts/sample-product-taxonomy.json)