"""
idea:
1) read each word and only consider [1:-1]
2) reverse it and check if it equals to original
3) if so, output the word

complexity: O(NxM) where N is number of words and M is number of characters of each word
"""

from absl import app

def main(argv):
    mid_p(argv[1])

def mid_p(filename):
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            mid = word[1:-1]
            if mid == mid[::-1]:
                print(word)
    return


if __name__ == '__main__':
    app.run(main)
