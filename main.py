import sys
import os


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
    for path in sys.argv[1:]:
        pass

    # start command prompt
    while True:
        print('search>', end=' ')
        query = input()
        if query == ':q':
            print('Terminating the program ...')
            sys.exit()


if __name__ == '__main__':
    main()
