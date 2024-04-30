import sys
import json
from rdflib import Graph, Namespace, Literal

def skos_to_json(skos_data):
    # Load the RDF data from a file
    g = Graph()
    g.parse(skos_data, format='turtle')  # Load Turtle formatted data

    # Define SKOS namespace
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

    # Prepare the JSON output structure
    concepts = []

    # Iterate over all concepts in the SKOS data
    for concept in g.subjects(SKOS.inScheme, None):
        concept_data = {
            "conceptID": str(concept),
            "prefLabel": "",
            "altLabels": [],
            "definition": "",
            "notes": "",
            "inScheme": [],
            "topConceptOf": False,
            "narrower": []
        }

        # Get preferred labels
        for label in g.objects(concept, SKOS.prefLabel):
            concept_data["prefLabel"] = str(label)

        # Get alternative labels
        for alt_label in g.objects(concept, SKOS.altLabel):
            concept_data["altLabels"].append(str(alt_label))

        # Get definitions
        for definition in g.objects(concept, SKOS.definition):
            concept_data["definition"] = str(definition)

        # Check if it is a top concept
        if any((concept, SKOS.topConceptOf, scheme) for scheme in g.objects(concept, SKOS.topConceptOf)):
            concept_data["topConceptOf"] = True

        # Get narrower concepts
        for narrower in g.objects(concept, SKOS.narrower):
            concept_data["narrower"].append(str(narrower))

        # Add concept data to list
        concepts.append(concept_data)

    return concepts

def main(input_file):
    # Convert SKOS to JSON
    json_output = skos_to_json(input_file)

    # Print JSON with proper formatting and double quotes
    print(json.dumps(json_output, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_turtle_file>")
        sys.exit(1)
    main(sys.argv[1])
