"""
idea:
1) read each line, split it, and check for Cost and Recommended
2) if meet requirements, all the splited line to a bigger list
3) after reading all lines, sort the bigger list by first column

complexity: O(NlogN) where N is number of lines
"""

from absl import app

def main(argv):
    reasonable_cost(argv[1])

def reasonable_cost(file):
    want = []
    header = ''
    with open(file, 'r') as f:
        header = f.readline()
        for line in f:
            words = line.split()

            # get the number and cut off the dollar sign
            cost = float(words[2][1:])
            if cost >= 20 and cost <= 50 and words[3] == 'Yes':
                want.append(words)
    sorted_want = sorted(want, key=lambda i: i[0], reverse=True)
    print(header, end='')
    for line in sorted_want:
        print(' '.join(line))
    return

if __name__ == '__main__':
    app.run(main)
