"""
idea:
1) check if len(a) and len(b) are different by >= 2 chars, if so return false
2) check if len(a) == len(b), if so compare char by char and only allow one char diff, if over one char diff, return false
3) check if len(a) and len(b) are different by 1 char, then we put the longer string into a, shorter into b.
4) then step thru both strings, if found a diff char, add a '_' to b and keep going, if found another diff char, return false

complexity: O(N) for N is the number of characters in longer string
"""

import sys

def almost_equal(a, b):
    if a == b:
        return False
    # len(a) and len(b) different by >= 2 chars
    if len(a) - len(b) > 1 or len(b) - len(a) > 1:
        return False

    # a and b have the same length
    if len(a) == len(b):
        quota_used = False
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                if quota_used:
                    return False
                quota_used = True
            i += 1
        return True
    
    # len(a) and len(b) different by only 1 char
    if len(a) < len(b):
        a, b = b, a
    i = 0 
    quota_used = False
    len_b = len(b)
    # only traverse the shorter length and deal with last char differently
    while i < len_b:
        if a[i] != b[i]:
            if quota_used:
                return False
            quota_used = True
            b = b[:i] + '_' + b[i:]
        i += 1
    if not quota_used:
        return True
    elif a[i] == b[i]:
        return True
    else:
        return False


print(almost_equal(sys.argv[1], sys.argv[2]))
