"""
idea:
1) sort the input string so then it's in alphabetical order
2) create a defaultdict for ease of storing 
3) scan are letters and sort the dict on value
4) print out the first three keys

complexity: O(NlogN) where N is the number of characters
"""

from absl import app
from collections import defaultdict

def main(argv):
    company_logo(argv[1])

def company_logo(s):
    letters = sorted(s)
    dd = defaultdict(int)
    for l in letters:
        dd[l] += 1
    s_l = sorted(dd.items(), key=lambda l:l[1], reverse=True) 
    for k,v in s_l[:3]:
        print(k + ' ' + str(v))

if __name__ == '__main__':
    app.run(main)
