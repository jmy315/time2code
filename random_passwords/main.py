"""
idea:
1) make a RE pattern for the password
2) check each line and see if it matches
3) if so, store it to set, if not, continue
4) print out the set

complexity: O(N) where N is number of lines
"""

from collections import OrderedDict
from absl import app
import re

def main(argv):
    random_passwords(argv[1])

def random_passwords(file):
    pw = OrderedDict()
    p = r'^([a-z0-9]{4}\-){2}[a-z0-9]{4}$'
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if re.match(p, line):
                if line in pw:
                    pw[line] = False
                else:
                    pw[line] = True
    for k,v in pw.items():
        if v:
            print(k)

if __name__ == '__main__':
    app.run(main)
