"""
idea:
1) we probably don't need the first line
2) read each line, if it's in the dict, append the price, if not, create a new key
3) print out the dict

complexity: O(N) where N is number of lines 
"""
from collections import OrderedDict
from absl import app

def main(argv):
    net_price(argv[1])

def net_price(file):
    o_dic = OrderedDict()
    with open(file, 'r') as f:
        f.readline()
        for line in f:
            words = line.split()
            item = ' '.join(words[:-1])
            price = words[-1]
            if item not in o_dic:
                o_dic[item] = 0
            o_dic[item] += int(price)
    for k, v in o_dic.items():
        print(k + ' ' + str(v))


if __name__ == '__main__':
    app.run(main)
