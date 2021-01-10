import os
import sys

def file_manipulation(dir_name):
    files = []
    try:
        entries = os.listdir(dir_name)
    except IOError:
        print(f'Cannot open dir: {dir_name}')
        return None
    os.chdir(dir_name)
    for entry in entries:
        if entry.endswith('.html'):
            try:
                os.rename(entry, entry[:-1])
            except IOError:
                print(f'Cannot rename {entry} to {entry[:-1]}')
        if entry.endswith('.jpg'):
            try:
                os.rename(entry, 'pictures/' + entry)
            except IOError:
                print(f'Cannot move {entry} to pictures/{entry}')
        if entry.endswith('.txt'):
            files.append(entry)
    files.sort()
    with open('stuff.txt', 'w') as f:
        try:
            for entry in files:
                with open(entry, 'r') as f2:
                    f.write(f2.read())
        except IOError:
            print(f'Cannot open file: {entry}')
    return None

file_manipulation(sys.argv[1])
