"""
idea:
1) read all contents of the file and store them to a list
2) if find queue, split that line and store into another list
3) if find succeeded or failed, remove them
4) the rest of lines should states the same
5) write back the header, queued lines and the rest of lines back to the file

Complexity: O(NlogN) where N is number of lines
"""

import sys

def update_queue(filename):
    queued_b = []
    new_data = []
    header = ''
    with open(filename, 'r') as f:
        header = f.readline()
        for line in f.readlines():
            if 'queued' in line:
                words = line.split()
                queued_b.append((words[0], words[1] + ' ' + words[2], words[3]))
            elif 'succeeded' not in line and 'failed' not in line:
                new_data.append(line)
    queued_b = sorted(queued_b, key=lambda x:x[1])
    with open(filename, 'w') as f:
        f.write(header)
        for words in queued_b:
            f.write(' '.join(words) + '\n')
        for line in new_data:
            f.write(line)
    return
        

update_queue(sys.argv[1])
