# Concept Validation

## Steps

### Create a Conda environment

```sh
conda create -n "concepts" python=3
conda activate python
pip install jsonschema
```

The first file is the file to validate.  The second file is the schema file:

```sh
python validate-concepts.py my-glossary.json concept-schema.json
```

```
JSON data is valid.
```