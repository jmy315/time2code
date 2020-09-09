"""
idea:
1) list test_dir to get all files
2) check the size of each file and remove whose size are < 3KB

complexity: O(N) where N is num of files
"""

import os
from absl import app

def main(argv):
    rm_small_files(argv[1])

def rm_small_files(dir):
    files = os.listdir(dir)
    rm_files = set()
    print(dir, '/')
    for file in sorted(files):
        size = os.stat(dir + '/' + file).st_size / 1024
        print('{} {:.1f}KB'.format(file, size)) 
        if size < 3:
            rm_files.add(file)
    print()
    for file in rm_files:
        print(file, 'removed!')
        os.remove(dir + '/' + file)

if __name__ == '__main__':
    app.run(main)
