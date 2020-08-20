"""
idea:
1) read each line save it as a list
2) use a list to store all the lines (list of lists)
3) sort the list by 1st and 2nd column
4) write the list back to a new file adding a new asset# columnn

complexity: O(NlogN) where N is number of lines
"""

from absl import app
from datetime import datetime

def main(argv):
    sort_assets(argv[1])

def sort_assets(file):
    big_list = []
    with open(file, 'r') as f1, open('new_assets', 'w') as f2:
        f2.write('Asset# ' + f1.readline())
        big_list = [line.split() for line in f1]
        big_list = sorted(big_list, key=lambda i:(i[0], datetime.strptime(i[1], '%m/%d/%Y')))
        for i in range(len(big_list)):
            f2.write(str(i+1).zfill(6) + ' ' + ' '.join(big_list[i]) + '\n')
    return

if __name__ == '__main__':
    app.run(main)
            

