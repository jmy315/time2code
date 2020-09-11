"""
idea:
1) use generator comprehension to go throug lines in file
2) get the sum and count the total number
3) print out the sum/count

complexity: O(N) where N is number of lines
"""

import sys

def get_avg(file):
    num_gen = (int(line.strip()) for line in open(file, 'r'))
    count = 0
    sum = 0
    for num in num_gen:
        sum += num
        count += 1
    return sum/count

print(get_avg(sys.argv[1]))
