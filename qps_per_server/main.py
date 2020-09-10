"""
idea:
1) create a dict {server -> counter} to store queries
2) keep a set to keep track how many seconds are in total
3) get len of set to get total seconds
4) calcult qps per server and output

complexity: O(NlogN) where N is number lines
"""

from absl import app

def main(argv):
    qps_per_server(argv[1])

def qps_per_server(log):
    servers = dict()
    sec = set()
    with open(log, 'r') as f:
        f.readline()
        for line in f:
            words = line.split()
            sec.add(words[0])
            if words[2] not in servers:
                servers[words[2]] = 0
            servers[words[2]] += 1
    total_sec = len(sec)
    sorted_servers = sorted(servers.items(), key=lambda i:i[0])
    print('Server_ID QPS')
    for s,c in sorted_servers:
        print('{0} {1:.1f}'.format(s, c/total_sec))

if __name__ == '__main__':
    app.run(main)
    
