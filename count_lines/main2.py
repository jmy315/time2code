import re
import sys

def count_lines(filename):
    counter = 0
    try:
        with open(filename, 'r') as f:
            # match ^ and $ only once
            p1 = '^\^.*\$\n$'
            # match multiple ^ and $
            p2 = '^\^\^+.*\$\$+\n$'
            for line in f:
                if line == '\n' or (re.match(p1, line) and not re.match(p2, line)):
                    continue
                counter += 1
    except OSError:
        print(f'Cannot open file: {filename}')
    return counter

print(count_lines(sys.argv[1]))
