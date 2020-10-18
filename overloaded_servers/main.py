"""
idea:
1) read the server name and date, and metrics
2) use three variables(for CPU, RAM, Disk) to keep track of loads 
3) each variable should be like this [start time, end_time, count_min) 
4) once we saw a new load that's < 80, we print out the info for the variable and reset it.

complexity: O(N) where N is the number of lines
"""

import sys

def overload(logname):
    server = ''
    cpu_load = [0,0,0]
    ram_load = [0,0,0]
    disk_load = [0,0,0]
    with open(logname, 'r') as f:
        for line in f:
            words = line.split()
            server = words[0]
            date = words[1] + ' ' + words[2]
            cpu = words[3]
            ram = words[4]
            disk = words[5]
            cpu_load = helper(server, 'CPU', date, cpu_load, cpu)
            ram_load = helper(server, 'RAM', date, ram_load, ram)
            disk_load = helper(server, 'Disk', date, disk_load, disk)
    if cpu_load[2] >= 3:
        print("Warning: {} CPU load is over 80% from {} to {}".format(server, cpu_load[0], cpu_load[1]))
    if ram_load[2] >= 3:
        print("Warning: {} RAM load is over 80% from {} to {}".format(server, ram_load[0], ram_load[1]))
    if disk_load[2] >= 3:
        print("Warning: {} Disk load is over 80% from {} to {}".format(server, disk_load[0], disk_load[1]))
    return

def helper(server, type, date, data, load):
    if float(load) >= 0.8:
        if data[2] > 0:
            data[1] = date
            data[2] += 1
        else:
            data[0] = date
            data[2] = 1
    else:
        if data[2] >= 3:
            print("Warning: {} {} load is over 80% from {} to {}".format(server, type, data[0], data[1]))
        data = [0, 0, 0]
    return data 

overload(sys.argv[1])
