# Concept Validation

CoPilot's SupportAI also supports the loading of SKOS-style concepts into the graph.
These concepts can be used to compose queries that use Boolean operations such as AND/OR/NOT
on collections.

Concepts can be as simple as a file of business terms.

[Financial Fraud Concepts](https://github.com/dmccrearytg/c360/blob/main/data/concepts/financial-fraud-concepts.json)

## Getting Started

### Create a Conda Environment With Required Libraries

We will need two libraries:

1. jsonschema
2. argparse
3. rdflib

```sh
conda create -n "concepts" python=3
conda activate python
pip install jsonschema argparse rdflib

## Steps

1. We will create a Python program that validates a simple flat Concepts file.
2. We will validate the file with a JSON schema file
3. We will then be able to validate that a Concepts file has the three required fields

## JSON Schema File

This schema file defines the fields and creates a definition for each field.

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

[Link to Shema File](https://github.com/dmccrearytg/c360/blob/main/data/concepts/concept-schema.json)


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