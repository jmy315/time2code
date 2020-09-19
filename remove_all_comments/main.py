"""
idea:
1) read each line, if see '"""', continue to read lines until sees '"""' again,
2) if see #, just read next line
3) for any line, write to our new file

complexity: O(N) where N is number of lines
"""

import sys

def remove_all_comments(code):
    in_comment = False
    with open(code, 'r') as f1, open('my_new_code.py', 'w') as f2:
        for line in f1.readlines():
            if in_comment:
                if line.strip().endswith('"""'):
                    in_comment = False
                continue
            if line.strip().startswith('"""'):
                in_comment = True
                continue
            if line.strip().startswith('#'):
                continue
            f2.write(line)
    return





remove_all_comments(sys.argv[1])
