"""
idea:
1) create a regex pattern for the license format
2) go through each line in the file and check if it match regex pattern
3) if match, print them out

complexity: O(N) where N is number of lines
"""

import sys
import re

def check_license(filename):
    # (?!\1) means negative lookahead in 1st capture group 
    # i.e. different from the previous digit
    p = r'^[1-9][A-HJ-NP-Z]{3}(\d)((?!\1)\d{2})$'
    with open(filename, 'r') as f:
        for line in f:
            license = line.strip()
            if re.match(p, license):
                print(license)
    return

check_license(sys.argv[1])
