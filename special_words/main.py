"""
idea:
1) create a RE pattern to match 'he' and 'er'
2) scan thru lines and find matchs and store them into a list
3) sort the list and print them out

complexty: O(NlogN) for N is the number of lines
"""

import sys
import re

def special_words(filename):
    p = r'^((he.*)|h)er.*$'
    matches = []
    with open(filename, 'r') as f:
        for line in f:
            if re.match(p, line.strip()):
                matches.append(line.strip())
    print(sorted(matches))
    return

special_words(sys.argv[1])
