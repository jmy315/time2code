"""
ideas:
1) read file1, use dict {name -> space_used}
2) read file2, update dict {name -> space_used / total_space}
3) dict to list and sort the list by usage percentage

complexity: O(NlogN) for N is the number of lines max(file1, file2)
"""

import sys

def sort_space(file1, file2):
    server_map = dict()
    try:
        with open(file1, 'r') as f:
            f.readline()
            for line in f.readlines():
                words = line.split()
                server = words[0]
                used = float(words[2])
                if server not in server_map.keys():
                    server_map[server] = 0
                server_map[server] = used
    except IOError:
        print('Failed to open: ' + file1)
        return False
    try:
        with open(file2, 'r') as f:
            f.readline()
            for line in f.readlines():
                words = line.split()
                server = words[0]
                total = float(words[2])
                if server not in server_map.keys():
                    continue
                server_map[server] /= total
    except IOError:
        print('Failed to open: ' + file2)
        return False

    server_list = server_map.items()
    sorted_list = sorted(server_list, key=lambda i: i[1], reverse=True)
    for i in sorted_list:
        if i[1] <= 1:
            print(i[0])
    return True


sort_space(sys.argv[1], sys.argv[2])
