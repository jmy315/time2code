"""
idea:
1) since only one user can access a file at a time, we don't need to check open or close, we only care about the file was seen first and second time.
2) create a dict named time_map {file -> [t1, t2, t3,...]}
3) note that we want t2 - t1, t4 - t3, ... as our access time
4) for each item in time_map, accumulate i+1 time - i time and store the avg time into a new dict name avg_map {file -> avg_time}
5) sorted the dic items and print out

complexty: O(NlogN) where N is number of lines
"""

from datetime import datetime, timedelta
import sys

def print_avg_access_time(log_file):
    time_map = dict()
    with open(log_file, 'r') as f:
        for line in f.readlines():
            entries = line.split()
            time_str = entries[0] + ' ' + entries[1]
            filename = entries[3]
            if filename not in time_map:
                time_map[filename] = []
            time_map[filename].append(time_str)
    avg_map = dict()
    for filename, time_list in time_map.items():
        total_time  = timedelta()
        avt_time = timedelta()
        for i in range(0,len(time_list),2):
            close_time = datetime.strptime(time_list[i+1], '%H:%M:%S %m-%d-%Y')
            open_time = datetime.strptime(time_list[i], '%H:%M:%S %m-%d-%Y')
            diff_time = close_time - open_time
            total_time += diff_time
        avg_time = timedelta(seconds=int(total_time.total_seconds()/(len(time_list)/2)))
        avg_map[filename] = str(avg_time)
    for i,j in sorted(avg_map.items(), key=lambda t:t[1]):
        print(i + ' ' + j)

print_avg_access_time(sys.argv[1])
