"""
idea:
1) use read() to count the total number of lines n
2) if n is even, read the (n/2-1)th and n/2th lines
3) if n is odd, read the n/2th line

complexity: O(N) where N is number of lines
"""

import sys

def print_median(file):
    n = 0
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            n += 1

    with open(file, 'r') as f:
        temp = ''
        for i in range(int(n/2)):
            temp = f.readline()
        if n % 2 == 0:
            print(temp, end='')
        print(f.readline(), end='')
    return

print_median(sys.argv[1])
