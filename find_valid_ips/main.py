"""
idea:
1) create an RE template  
2) find all matches
3) print out valid IPs

complexity: O(N) where N is number of lines
"""

from absl import app
import re

def main(argv):
    find_valid_ips(argv[1])

def find_valid_ips(file):
    t = re.compile('^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
    with open(file, 'r') as fd:
        for ip in fd:
            if re.match(t, ip):
                print(ip, end='')


if __name__ == '__main__':
    app.run(main)

