"""
idea:
1) create a generator method to read thru files line by line
2) Traverse both files line by line and compare if they the same
3) if yes, continue, else, return False right away

complexity:O(N) where is the number of lines of the larger file
"""

import os
import sys
from itertools import zip_longest

def file_gen(file):
    return((line for line in open(file, 'r')))

def comp(file1, file2):
    size1 = os.stat(file1).st_size
    size2 = os.stat(file2).st_size
    if size1 != size2:
        return False
    gen1 = file_gen(file1)
    gen2 = file_gen(file2)
    for a, b in zip_longest(gen1, gen2):
        if a != b:
            return False
    return True

print(comp(sys.argv[1], sys.argv[2]))
