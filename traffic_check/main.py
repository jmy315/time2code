"""
idea:
1) create a dict for service and a dict for cell
2) each dict value is a list of length [total_qps, total_throughput]
3) print out both dicts

complexity: O(N) where N is number of lines
"""

import sys

def traffic_check(logfile):
    cell_dict = dict()
    service_dict = dict()
    with open(logfile, 'r') as f:
        f.readline()
        for line in f.readlines():
            words = line.split()
            service = words[0]
            cell = words[1]
            qps = int(words[2])
            thru = int(words[3])
            if cell not in cell_dict.keys():
                cell_dict[cell] = [0, 0]
            cell_dict[cell][0] += qps
            cell_dict[cell][1] += thru
            
            if service not in service_dict.keys():
                service_dict[service] = [0, 0]
            service_dict[service][0] += qps
            service_dict[service][1] += thru
    for k, v in cell_dict.items():
        print('Cell: {}, QPS: {}, Throughput(Mbps): {}'.format(k, v[0], v[1]))
    for k, v in service_dict.items():
        print('Service: {}, QPS: {}, Throughput(Mbps): {}'.format(k, v[0], v[1]))
    return

traffic_check(sys.argv[1])
