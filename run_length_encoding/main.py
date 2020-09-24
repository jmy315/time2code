"""
idea:
1) read each character, if not seen, keep going until a new character shows up
2) print out the number and old char when a new char is seen

complexity: O(N) where N is number of characters
"""

def run_length(s):
    i = 0
    while i < len(s):
        num = 0
        while i < len(s)-1 and s[i] == s[i+1]:
            num += 1
            i += 1
        print(str(num+1) + s[i], end='')
        i += 1
    print()

run_length('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
