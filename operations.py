class DocumentOperation:
    def execute(self, document):
        pass

class AddDataOperation(DocumentOperation):
    def __init__(self, data):
        self.data = data

    def execute(self, document):
        document.data.update(self.data)

class RemoveDataOperation(DocumentOperation):
    def __init__(self, data_keys):
        self.data_keys = data_keys

    def execute(self, document):
        for key in self.data_keys:
            document.data.pop(key, None)
