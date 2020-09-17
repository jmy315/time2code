"""
idea:
1) create a generator method to read thru files line by line
2) Traverse both files line by line and compare if they the same
3) if yes, continue, else, return False right away

complexity:O(N) where is the number of lines of the larger file
"""

import sys

def file_gen(file):
    return((line for line in open(file, 'r')))

def comp(file1, file2):
    gen1 = file_gen(file1)
    gen2 = file_gen(file2)
    for a, b in zip(gen1, gen2):
        if a != b:
            return False
    for a in gen1:
        return False
    for a in gen2:
        return False
    return True

print(comp(sys.argv[1], sys.argv[2]))
