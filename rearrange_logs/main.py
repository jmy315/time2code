"""
idea:
1) read all lines and check each line
2) when seeing Get, Set, or Add, save the line to get_log, set_log, or add_log
3) create a dict for each function and use date as key, counter as value
4) once finish all lines, write the dict to stats_log

Complexity: O(N) where N is the number of all lines
"""

from absl import app

def main(argv):
    rearrange_logs(argv[1:])

def rearrange_logs(files):
    g_dic = {}
    s_dic = {}
    a_dic = {}
    with open('get_log', 'w') as f1, open('set_log', 'w') as f2, open('add_log', 'w') as f3:
        for file in files:
            with open(file, 'r') as f:
                for line in f:
                    call = line.split()[2]
                    date = line.split()[1]
                    if call == 'Get':
                        f1.write(line)
                        if date not in g_dic:
                            g_dic[date] = 0
                        g_dic[date] += 1
                    elif call == 'Set':
                        f2.write(line)
                        if date not in s_dic:
                            s_dic[date] = 0
                        s_dic[date] += 1
                    else:
                        f3.write(line)
                        if date not in a_dic:
                            a_dic[date] = 0
                        a_dic[date] += 1
    with open('stats_log', 'w') as f4:
        f4.write('Get\n')
        for k,v in g_dic.items():
            f4.write(k + ' ' + str(v) + '\n')
        f4.write('Set\n')
        for k,v in s_dic.items():
            f4.write(k + ' ' + str(v) + '\n')
        f4.write('Add\n')
        for k,v in a_dic.items():
            f4.write(k + ' ' + str(v) + '\n')
    return

if __name__ == '__main__':
    app.run(main)
