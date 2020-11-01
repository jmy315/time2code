"""
idea:
1) read the file line by line, keep a list to store the tuple of percentage of 'apple' per line and the line itself
2) then sort the list by the percentage
3) write the sorted lines into a new file

comlexity: O(NlogN) where N is the number of lines
"""

import sys

def sort_by_apple(filename, word):
    percent_and_lines = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                fruits = line.strip().split(',')
                count = 0
                total = len(fruits)
                for fruit in fruits:
                    if fruit == word:
                        count += 1
                percent_and_lines.append((count/total, line))
    except IOError:
        print('Unable to open {}'.format(filename))
        return False

    sorted_percent_and_lines = sorted(percent_and_lines, key=lambda i:i[0], reverse=True)

    try:
        with open('new_file', 'w') as f:
            for _, line in sorted_percent_and_lines:
                f.write(line)
    except IOError:
        print('Unable to open new_file')
        return False
    return True

sort_by_apple(sys.argv[1], 'apple')
