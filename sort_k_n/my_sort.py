"""
idea:
1) read the file save all lines in a list
2) used sorted to sort the col column
3) print out the list after sorted

complexity: O(NlogN) where N is number of lines
"""

import sys

def my_sort(filename, col):
    with open(filename, 'r') as f:
        data = [line.split() for line in f.readlines()]
        sorted_data = data
        if col > 0 and col <= len(data[0]):
            try:
                sorted_data = sorted(data, key=lambda i:int(i[col-1]))
            except ValueError:
                print('data in column {} is NOT numeric, please try to sort with a different column'.format(col))
                return
        for items in sorted_data:
            print(' '.join(items))
    return

my_sort(sys.argv[1], int(sys.argv[2]))
