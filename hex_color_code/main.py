"""
idea
1) create an RE pattern 
2) read each line and if it matches the pattern, check if it's at the beginning 
of the line. If so, drop it
3) print valid color code

complexity: O(NxM) where N is # of lines and M is # of words per line
"""
from absl import app
import re

def main(argv):
    hex_color(argv[1])

def hex_color(file):
    p = '#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?'
    with open(file, 'r') as f:
        for line in f:
            if re.match(p, line):
                continue
            found = re.findall(p, line)
            if found:
                for i in found:
                    print(i)

if __name__ == '__main__':
    app.run(main)
