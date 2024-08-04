from document import TypeADocument, TypeBDocument

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'TypeA':
            return TypeADocument()
        elif doc_type == 'TypeB':
            return TypeBDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")
