"""
idea:
1) use OrderedDict for this because output is based on appearannce order
2) read each line and save the word as key to the dict
3) if seen, value +1, else, value is 1
4) print out the dict

complexity: O(N) where N is number of lines
"""
from collections import OrderedDict
from absl import app

def main(argv):
    word_order(argv[1])

def word_order(file):
    o_dic = OrderedDict()
    with open(file, 'r') as fd:
        fd.readline() # omit the first line
        for line in fd:
            word = line.strip()
            if word not in o_dic:
                o_dic[word] = 0
            o_dic[word] += 1
    print(len(o_dic))
    print(' '.join(map(str, o_dic.values())))

if __name__ == '__main__':
    app.run(main)
