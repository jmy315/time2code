"""
idea:
1) use dict (pid -> [start, end]) to store time spent
2) calculate time spent for each pid and store (pid, time spent) to a list
3) sort the list by pid and print them

complexity: O(NlogN) where N is number of lines
"""

from absl import app
from datetime import datetime

def main(argv):
    clear_up(argv[1])

def clear_up(file):
    dic = {}
    with open(file, 'r') as f:
        f.readline()
        for line in f:
            words = line.split()
            if words[2] not in dic:
                dic[words[2]] = []
            dic[words[2]].append(words[0] + ' ' + words[1])
        for pid, t in sorted(dic.items(), key=lambda i:i[0]):
            print(pid + ' ' + cal_time(t[0], t[1]))
    return

def cal_time(a, b):
    ta = datetime.strptime(a, '%H:%M:%S %m/%d/%Y')
    tb = datetime.strptime(b, '%H:%M:%S %m/%d/%Y')
    d = tb - ta
    return str(d)

if __name__ == '__main__':
    app.run(main)
