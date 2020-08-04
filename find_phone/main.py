"""
idea:
1) create RE pattern
2) read each line and search with pattern
3) print out valid numbers

complexity: O(N) where N is number of lines
"""

from absl import app
import re

def main(argv):
    find_phone(argv[1])

def find_phone(file):
    p = '^(([0-9]{3}[\.|\s|-]){2}[0-9]{4})|(\([0-9]{3}\)\s[0-9]{3}[\s|-][0-9]{4})$'
    with open(file, 'r') as fd:
        for line in fd:
            phone = ' '.join(line.split()[2:])
            if re.match(p, phone):
                print(phone)

if __name__ == '__main__':
    app.run(main)
