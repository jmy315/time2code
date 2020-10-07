"""
idea:
1) create a dict to store item -> [num of 4+, total num]
2) go thru the file and add them to the dict
3) print out item and percentage

complexity: O(N) where N is the number of lines
"""

import sys

def over_price(filename):
    p_map = dict()
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            price = float(words[-1][1:])
            item = words[0]
            if item not in p_map:
                p_map[item] = [0,0]
            if price > 4:
                p_map[item][0] += 1
            p_map[item][1] += 1
    for k, v in p_map.items():
        print('{}: {:.1f}%'.format(k, v[0]/v[1]*100)) 

over_price(sys.argv[1])
