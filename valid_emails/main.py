"""
idea:
1) create a good regex pattern to filter emails
2) read through the input file line by line and see if there's a match
3) if so, print out the email address

complexity: O(N) where N is the number of lines
"""

from absl import app
import re

def main(argv):
    valid_emails(argv[1])

def valid_emails(file):
    p = r'^[0-9A-Za-z]([0-9A-Za-z]|\-)*@[A-Za-z]+\.(com|net|edu|gov)$'    
    with open(file, 'r') as fd:
        fd.readline() # skip the header
        for line in fd:
            # get the third column as email address
            email = ' '.join(line.split()[2:])
            if re.match(p, email):
                print(email)
    return

if __name__ == '__main__':
    app.run(main)
