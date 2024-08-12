import json
import os

class SpecLoaderError(Exception):
    pass

def load_spec(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Spec file not found: {file_path}")

    try:
        with open(file_path, 'r') as file:
            spec = json.load(file)
    except json.JSONDecodeError:
        raise SpecLoaderError(f"Failed to decode JSON from the spec file: {file_path}")

    required_keys = {"ColumnNames", "Offsets", "FixedWidthEncoding", "IncludeHeader", "DelimitedEncoding"}
    if not required_keys.issubset(spec.keys()):
        raise SpecLoaderError(f"Invalid spec file: Missing required keys {required_keys - set(spec.keys())}")

    return spec
