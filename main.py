import argparse
import json
from factory import DocumentFactory
from operations import AddDataOperation, RemoveDataOperation

def main():
    parser = argparse.ArgumentParser(description="Document Manager")
    subparsers = parser.add_subparsers(dest='command')

    # Initialize document
    init_parser = subparsers.add_parser('init')
    init_parser.add_argument('doc_type', type=str, help='Type of document')

    # Modify document
    mod_parser = subparsers.add_parser('modify')
    mod_parser.add_argument('doc_type', type=str, help='Type of document')
    mod_parser.add_argument('action', type=str, choices=['add_data', 'remove_data'], help='Action to perform')
    mod_parser.add_argument('--data', type=json.loads, help='Data to add')
    mod_parser.add_argument('--keys', type=json.loads, help='Data keys to remove')

    args = parser.parse_args()

    if args.command == 'init':
        document = DocumentFactory.create_document(args.doc_type)
        document.save(f'documents/{args.doc_type}/doc.json')
        print(f"{args.doc_type} document created.")

    elif args.command == 'modify':
        document = DocumentFactory.create_document(args.doc_type)
        operation = None
        if args.action == 'add_data':
            operation = AddDataOperation(args.data)
        elif args.action == 'remove_data':
            operation = RemoveDataOperation(args.keys)
        
        if operation:
            operation.execute(document)
            document.save(f'documents/{args.doc_type}/doc.json')
            print(f"{args.doc_type} document modified.")

if __name__ == "__main__":
    main()
