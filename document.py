import json
from utils import load_template  # Ensure this import is correct based on your utils.py location

class Document:
    def __init__(self, layout, data):
        self.layout = layout
        self.data = data

    def save(self, path):
        with open(path, 'w') as f:
            json.dump({
                "layout": self.layout,
                "data": self.data
            }, f, indent=4)

class TypeADocument(Document):
    def __init__(self):
        layout = load_template('templates/layout_templates/typeA_layout.json')
        data = load_template('templates/data_templates/typeA_data.json')
        super().__init__(layout, data)

class TypeBDocument(Document):
    def __init__(self):
        layout = load_template('templates/layout_templates/typeB_layout.json')
        data = load_template('templates/data_templates/typeB_data.json')
        super().__init__(layout, data)
