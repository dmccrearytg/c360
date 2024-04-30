import json
from rdflib import Graph, URIRef, Namespace

def skos_to_json(skos_data):
    # Load the RDF data from a file or a string
    g = Graph()
    g.parse(data=skos_data, format='turtle')  # assuming input is in Turtle format

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
        if (concept, None, None) in g:
            concept_data["topConceptOf"] = True

        # Get narrower concepts
        for narrower in g.objects(concept, SKOS.narrower):
            concept_data["narrower"].append(str(narrower))

        # Add concept data to list
        concepts.append(concept_data)

    return json.dumps(concepts, indent=4)

# Example SKOS data as a Turtle string (for demonstration)
skos_data = """
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex: <http://example.com/ns#> .

ex:Beverage a skos:Concept ;
    skos:prefLabel "Beverage" ;
    skos:altLabel "Drink" ;
    skos:definition "A liquid for drinking" ;
    skos:inScheme ex:Scheme ;
    skos:narrower ex:Tea .

ex:Tea a skos:Concept ;
    skos:prefLabel "Tea" ;
    skos:altLabel "Brew" ;
    skos:definition "A hot beverage made by steeping tea leaves in water" ;
    skos:inScheme ex:Scheme ;
    skos:narrower ex:GreenTea .

ex:GreenTea a skos:Concept ;
    skos:prefLabel "Green Tea" ;
    skos:definition "Tea that has not undergone the same withering and oxidation process as black tea" ;
    skos:inScheme ex:Scheme .
"""

# Convert SKOS to JSON
json_output = skos_to_json(skos_data)
print(json_output)
