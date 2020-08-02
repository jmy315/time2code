"""
idea:
1) creat an RE pattern for valid MAC    
2) read each line and check if it matches the pattern
3) print matches

complexity: O(N) where N is number of lines
"""

import re
from absl import app

def main(argv):
    find_valid_mac_address(argv[1])

def find_valid_mac_address(file):
    p = '([0-9A-F]{2}\:){5}[0-9A-F]{2}'
    with open(file, 'r') as fd:
        fd.readline()
        for lines in fd:
            found = re.search(p, lines)
            if found:
                print(found.group(0))

if __name__ == '__main__':
    app.run(main)
