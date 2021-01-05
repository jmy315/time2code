import sys

def group_by_groupname(filename):
    group_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                group_list.append(line.split())
    except IOError:
        print(f'Cannot open file: {filename}')
        return None
    
    group_list.sort(key=lambda x: x[1])
    with open('newfile2', 'w') as f:
        for words in group_list:
            f.write(' '.join(words) + '\n')
    return None


group_by_groupname(sys.argv[1])
