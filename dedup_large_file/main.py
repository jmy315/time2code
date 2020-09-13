"""
idea: 
1) Note that we need generator for reading large file
2) Note that the order of reading lines matters, we will use OrderedDict here
3) Once we finish reading the whole, write the lines in the OD to a new file

complexity: O(N) where N is the number of lines
"""

from collections import OrderedDict
import sys

def dedup_large_file(file):
    line_gen = (line for line in open(file, 'r'))
    dic = OrderedDict()
    for line in line_gen:
        if line not in dic:
            dic[line] = True
        dic[line] = True
    with open('new_file', 'w') as f:
        for k,_ in dic.items():
            f.write(k)

dedup_large_file(sys.argv[1])
