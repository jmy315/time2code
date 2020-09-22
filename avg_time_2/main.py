"""
idea:
1) read each line and get time1 and time2 and diff 
2) turn diff into seconds and add them to total
3) total/num_of_lines to get average time

complexity: O(N) where N is number of lines
"""

from datetime import datetime, timedelta
import sys

def avg_time(filename):
    total_time = timedelta()
    total_lines = 0
    with open(filename, 'r') as f:
        for line in f:
            items = line.split()
            ts1 = items[1] + ' ' + items[2]
            ts2 = items[4] + ' ' + items[5]
            t1 = datetime.strptime(ts1, '%H:%M:%S %m/%d/%Y')
            t2 = datetime.strptime(ts2, '%H:%M:%S %m/%d/%Y')
            total_time += t2 - t1
            total_lines += 1
    print(timedelta(seconds=round(total_time.total_seconds()/total_lines)))


avg_time(sys.argv[1])
