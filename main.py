import sys
import os
from glob import glob

from database import Database
from invertedindex import InvertedIndex


def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def main():
    if len(sys.argv) < 2:
        sys.exit('Please, provide a valid system path')

    print('Validating dirs ...')
    for path in sys.argv[1:]:
        # validating the path is a dir
        if not os.path.isdir(path):
            sys.exit('{} is not a valid Dir path.'.format(path))

    # building the index
    print('start processing files in each dir ...')

    db = Database()
    index = InvertedIndex(db)

    document_id = 0
    for path in sys.argv[1:]:
        for _file in glob(path + '*.txt'):
            document_id += 1
            with open(_file, 'r') as input_file:
                index.index_document({
                    'id': document_id,
                    'text': input_file.read()
                })

    print('{} files are read and processed'.format(document_id))

    # start command prompt
    while True:
        print('search>', end=' ')
        query = input()
        if query == ':q':
            print('Terminating the program ...')
            sys.exit()
        result = index.lookup_query(query)
        for term in result.keys():
            for appearance in result[term]:
                document = db.get(appearance.docId)
                print(highlight_term(appearance.docId, term, document['text']))
            print("-----------------------------")


if __name__ == '__main__':
    main()
