"""
idea:
1) create a dict {inode -> [file1, file2]}
2) list all files under directory and get inodes of each file
3) get dict values, only keep one file in the list, remove the others

complexity: O(N) where N is the number of files under directory
"""

import sys
import os

def dedup_hardlinks(dir):
    inodes_map = dict()
    files = os.listdir(dir)
    for file in files:
        inode = os.lstat(dir + '/' + file).st_ino
        if inode not in inodes_map:
            inodes_map[inode] = []
        inodes_map[inode].append(file)
    for files in inodes_map.values():
        while len(files) > 1:
            os.remove(dir + '/' + files[-1])
            files = files[:-1]
    return

dedup_hardlinks(sys.argv[1])
