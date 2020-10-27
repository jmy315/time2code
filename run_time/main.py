"""
idea:
1) create a dict {PID -> [time_used, m_time]}
2) time_used was calculated before stored into the dict
3) keep a list on the side to store exited processes
4) print out PIDs and time_used at the time for exited processes

complexity: O(N) where N is number of lines
"""

import sys
from datetime import datetime, timedelta

def run_time(filename):
    pt_map = dict()
    exited_p = list()
    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            words = line.split()
            time_string = words[0] + ' ' + words[1]
            pid = words[2]
            act = words[3]
            time_obj = datetime.strptime(time_string, '%H:%M:%S %m/%d/%Y')
            if act == 'start':
                pt_map[pid] = [timedelta(0), time_obj]
            if act == 'pause':
                pt_map[pid] = [pt_map[pid][0] + time_obj - pt_map[pid][1], time_obj]
            if act == 'resume':
                pt_map[pid] = [pt_map[pid][0], time_obj]
            if act == 'exit':
                exited_p.append(pid)
                pt_map[pid] = [pt_map[pid][0] + time_obj - pt_map[pid][1], time_obj]
        for pid in exited_p:
            print('{}: {}'.format(pid, pt_map[pid][0]))
    return

run_time(sys.argv[1])
