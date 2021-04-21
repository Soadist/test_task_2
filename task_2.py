import hashlib
import sys


def check_file(check_item):
    filename = check_item[0]
    method = check_item[1]
    try:
        with open(CHECK_DIR+'/'+filename, 'rb') as f:
            file_hash = getattr(hashlib, method)()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        if file_hash.hexdigest().lower() == check_item[2].lower():
            return filename + ' OK'
        return filename + ' FAIL '
    except FileNotFoundError:
        return filename + ' NOT FOUND'
    except IsADirectoryError:
        return filename + ' DIR NOT FILE'
    except PermissionError:
        return filename + ' ACCESS DENIED'


if __name__ == '__main__':
    try:
        INPUT_FILE = sys.argv[1]
        CHECK_DIR = sys.argv[2]
    except IndexError:
        print('Syntax')
        print(
            'python task_2.py <path to the input file>'
            ' <path to the directory containing the files to check>'
        )
        exit()
    try:
        with open(INPUT_FILE, 'r') as f:
            while row := f.readline():
                if row.isspace():
                    continue
                row = row.rstrip('\n').split()
                check_item = ['', '', '']
                check_item[2] = row.pop(-1)
                check_item[1] = row.pop(-1)
                check_item[0] = ' '.join(row)
                print(check_file(check_item))
    except FileNotFoundError:
        print(str(INPUT_FILE + ' NOT FOUND'))
    except IsADirectoryError:
        print(str(INPUT_FILE + ' DIR NOT FILE'))
    except PermissionError:
        print(str(INPUT_FILE + ' ACCESS DENIED'))
