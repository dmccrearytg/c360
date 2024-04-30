import json
import argparse
from jsonschema import validate
from jsonschema.exceptions import ValidationError

def load_json_file(filename):
    """ Load JSON data from a file. """
    with open(filename, 'r') as file:
        return json.load(file)

def validate_json(data, schema):
    """ Validate JSON data using the given schema. """
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid.")
    except ValidationError as e:
        print("JSON data is invalid.")
        print("Validation error:", e)

def main():
    parser = argparse.ArgumentParser(description="Validate JSON file against a JSON Schema.")
    parser.add_argument("json_file", help="Path to the JSON file that needs to be validated")
    parser.add_argument("schema_file", help="Path to the JSON schema file")

    args = parser.parse_args()

    # Load the data and the schema
    data = load_json_file(args.json_file)
    schema = load_json_file(args.schema_file)

    # Validate the loaded data against the schema
    validate_json(data, schema)

if __name__ == "__main__":
    main()
