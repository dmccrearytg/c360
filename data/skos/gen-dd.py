from rdflib import Graph, URIRef, Literal, Namespace

# Define namespaces
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
EX = Namespace("http://example.org/ns#")

# Create a new graph
g = Graph()

# Define Dewey Decimal top-level categories with additional details
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

# Populate the graph with SKOS concepts
for code, (label, alt_labels, definition) in categories.items():
    concept = URIRef(f"http://example.org/ns#{code}")  # Ensure URIRef is used for the concept
    g.add((concept, SKOS.prefLabel, Literal(label)))
    g.add((concept, SKOS.definition, Literal(definition)))
    g.add((concept, SKOS.inScheme, URIRef("http://example.org/ns#DeweyDecimalClassification")))
    g.add((concept, SKOS.topConceptOf, URIRef("http://example.org/ns#DeweyDecimalClassification")))
    for alt_label in alt_labels:
        g.add((concept, SKOS.altLabel, Literal(alt_label)))

# Serialize the graph to RDF/Turtle format
rdf_data = g.serialize(format="turtle")

# Write to a file
file_path = "dd-v2.ttl"
with open(file_path, "w") as f:
    f.write(rdf_data)

# close the file_path
