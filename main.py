import sys

from utils import process_docs, valid_pathes, perform_scored_search


def main():
    if len(sys.argv) < 2:
        sys.exit('Please, provide a valid system path')

    if not valid_pathes(sys.argv[1:]):
        sys.exit('{} is not a valid Dir path.'.format(path))

    db, index = process_docs(sys.argv[1:])

    # start command prompt
    while True:
        print('search (:q to exit) >', end=' ')
        query = input()
        if query == ':q':
            print('Terminating the program ...')
            sys.exit()

        perform_scored_search(db, index, query)


if __name__ == '__main__':
    main()
