import sys

def dedup_file(filename):
    file_dict = dict()
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line not in file_dict:
                    file_dict[line] = True
    except IOError:
        print(f'Cannot open file: {filename}')
        return None
    try:
        with open('newfile2', 'w') as f:
            for key in file_dict.keys():
                f.write(key)
    except IOError:
        print('Cannot create file: newfile2')
    return None

dedup_file(sys.argv[1])
