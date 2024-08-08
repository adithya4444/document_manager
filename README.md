# Document Manager

This project provides a flexible way to create and manage various document types using ChatGPT-powered Python scripts.

## Project Structure

```plaintext
document_manager/
├── templates/
│   ├── layout_templates/
│   │   ├── typeA_layout.json
│   │   ├── typeB_layout.json
│   └── data_templates/
│       ├── typeA_data.json
│       ├── typeB_data.json
├── documents/
│   ├── typeA/
│   │   ├── doc1.json
│   └── typeB/
│       ├── doc1.json
├── migrations/
│   ├── migration1.py
│   ├── migration2.py
├── document.py
├── factory.py
├── main.py
├── operations.py
└── utils.py
