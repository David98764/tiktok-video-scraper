thonimport json

def save_to_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    """Load data from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)