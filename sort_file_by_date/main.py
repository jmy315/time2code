"""
idea:
1) read the file and read line by line
2) reformat the date and store (date, filename) into a list
3) sort the list by date and print them

complexity: O(NlogN) where N is number of lines 
"""
from absl import app
from datetime import datetime

def main(argv):
    sort_file_by_date(argv[1])

def sort_file_by_date(file):
    li = []
    with open(file, 'r') as fd:
        for line in fd:
            words = line.split()
            date_str = ' '.join(words[2:5]) 
            filename = words[-1]
            date_object = datetime.strptime(date_str, '%B %d, %Y')
            li.append((date_str, date_object, filename))
    sorted_files = sorted(li, key=lambda d:(d[1]), reverse=True)
    for k,v,j in sorted_files:
        print(j + ', ' + k)
    return


if __name__ == '__main__':
    app.run(main)
