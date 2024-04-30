import json
import argparse

def convert_json_to_jsonl(input_file, output_file):
    """ Convert JSON array file to JSON Lines format. """
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    with open(output_file, 'w') as outfile:
        for entry in data:
            json_line = json.dumps(entry)
            outfile.write(json_line + '\n')

def main():
    parser = argparse.ArgumentParser(description="Convert JSON file to JSONL format.")
    parser.add_argument("input_file", help="Path to the input JSON file")
    parser.add_argument("output_file", help="Path to the output JSONL file")

    args = parser.parse_args()

    # Convert JSON to JSONL
    convert_json_to_jsonl(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
