import json

def load_template(path):
    with open(path, 'r') as f:
        return json.load(f)
