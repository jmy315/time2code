"""
idea:
1) create a dict { word -> count }
2) read each line and split it to words and add them to dict
3) print out the top 3 words from dict, and continue to check if the next word has the same count, if so continue to print out words until seeing a smaller count

complexity: O(NlogN) where N is number total words
"""

import sys
from collections import defaultdict

def top_three(filename):
    w_map = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                w_map[word] += 1
    counter = 0
    pre_count = 0
    for k, v in sorted(w_map.items(), key=lambda i:i[1], reverse=True):
        counter += 1
        if counter <= 3 or v == pre_count:
            print('{}: {}'.format(k, v))
            pre_count = v
    return

top_three(sys.argv[1])
