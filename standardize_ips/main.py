"""
idea:
1) create a RE pattern for just numbers
2) use re.findall get all numbers
3) remove leading zeros by convert all numbers from str to int 
4) form integers to IPs and write sorted IPs to a new file 

complexty: O(NlogN) where N is number of lines
"""

from absl import app
import re

def main(argv):
    standardize_ips(argv[1])

def standardize_ips(file):
    p = r'[0-9]{1,3}'
    with open(file, 'r') as f, open('newfile', 'w') as f2:
        for line in f:
            matches = re.findall(p, line)
            temp = []
            for match in matches:
                temp.append(str(int(match)))
            f2.write('.'.join(temp) + '\n')
    return       

if __name__ == '__main__':
    app.run(main)
