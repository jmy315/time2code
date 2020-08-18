"""
idea:
1) use dict to store 26 letters
2) check each k,v and if any key has seen
3) if so, move on, else, return false

complextiy O(MxN) where M is number of lines and N is number of letters in a sentence
"""

from absl import app
import string

def main(argv):
    pangrams(argv[1])

def pangrams(file):
    alpha = {}
    letters = list(string.ascii_lowercase)
    with open(file, 'r') as fd:
        for line in fd:
            for l in letters:
                alpha[l] = False
            for l in line.lower():
                if l in alpha:
                    alpha[l] = True
            yesno = ''
            for k,v in alpha.items():
                if not v:
                    yesno = 'not '
                    break
            print(yesno + 'pangram')
    return

if __name__ == '__main__':
    app.run(main)

