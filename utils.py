import os
from glob import glob
from collections import OrderedDict
from database import Database
from invertedindex import InvertedIndex


def valid_pathes(pathes):
    print('Validating dirs ...')
    for path in pathes:
        # validating the path is a dir
        if not os.path.isdir(path):
            return False
    return True


def process_docs(pathes):
    # building the index
    print('start processing files in each dir ...')

    db = Database()
    index = InvertedIndex(db)

    document_id = 0
    for path in pathes:
        for _file in glob(path + '*.txt'):
            document_id += 1
            with open(_file, 'r') as input_file:
                index.index_document({
                    'id': document_id,
                    'text': input_file.read(),
                    'name': _file
                })

    print('{} files are read and processed'.format(document_id))
    return db, index


def perform_scored_search(db, index, query):
    term_score = 100 / len(query.split())
    result = index.lookup_query(query)
    document_score = OrderedDict()
    for term in result.keys():
        for appearance in result[term]:
            if appearance.docId in document_score:
                document_score[appearance.docId] += term_score
            else:
                document_score[appearance.docId] = term_score

    counter = 1
    for i, score in document_score.items():
        if counter > 10:
            break
        document = db.get(i)
        print(document['name'], score, sep=' -- ')
        counter += 1
