# SKOS to JSON Format Conversion

```py
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
        print("Usage: python skos-to-json.py <input_turtle_file>")
        sys.exit(1)
    main(sys.argv[1])
```
## Sample Python Data

```py
categories = {
    "000": ("General works, Computer science and Information", 
            ["Generalities", "Books", "Libraries", "Internet"],
            "Books and other compilations that do not fit other categories, including computer science and information."),
    "100": ("Philosophy and psychology", 
            ["Metaphysics", "Ethics", "Aesthetics"],
            "Disciplines and studies that involve the nature of reality and existence, ethical and moral reasoning, and the mind."),
    "200": ("Religion", 
            ["Theology"],
            "Systematic and detailed discussions and theologies of various religions."),
    "300": ("Social sciences", 
            ["Sociology", "Anthropology", "Economics", "Law", "Public administration"],
            "Studies concerned with society and the relationships among individuals within a society."),
    "400": ("Language", 
            ["Linguistics", "Dictionaries"],
            "Concerns the structure and use of language."),
    "500": ("Science", 
            ["Mathematics", "Physics", "Chemistry", "Biology"],
            "Disciplines that involve the scientific study of the natural world and its phenomena."),
    "600": ("Technology", 
            ["Engineering", "Agriculture", "Home economics", "Management"],
            "Applied sciences and technologies, including health sciences, agriculture, and management."),
    "700": ("Arts and recreation", 
            ["Fine Arts", "Music", "Sports"],
            "Cultural and creative expressions through fine arts, entertainment, and sports."),
    "800": ("Literature", 
            ["Poetry", "Drama", "Fiction", "Essays"],
            "Works of creative writing, including poetry, drama, fiction, and essays."),
    "900": ("History and geography", 
            ["Historical books", "Geographic guides", "Biographies"],
            "Detailed accounts of historical events and comprehensive guides to geography and biographies.")
}
```

## Sample RDF File

```rdf
@prefix ns1: <http://www.w3.org/2004/02/skos/core#> .

<http://example.org/ns#000> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "General works, Computer science and Information" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#100> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Philosophy and psychology" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#200> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Religion" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#300> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Social sciences" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#400> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Language" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#500> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Science" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#600> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Technology" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#700> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Arts and recreation" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#800> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "Literature" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

<http://example.org/ns#900> ns1:inScheme <http://example.org/ns#DeweyDecimalClassification> ;
    ns1:prefLabel "History and geography" ;
    ns1:topConceptOf <http://example.org/ns#DeweyDecimalClassification> .

```

## Sample Output
