"""
idea:
1) walk dir1 and save all dirs/filenames to a dict
2) walk dir2 and check if each item has the same path and filename
3) if so, rename filename and move it to dir1
4) if not, simply move it to dir1

complexity: O(N) where N is number of dirs and files
"""

import os
import shutil
from absl import app

def main(argv):
    combine_dirs(argv[1], argv[2])

def combine_dirs(d1, d2):
    dir_dic = dict()
    for root, dirs, files in os.walk(d1):
        for file in files:
            sub_dir = '/'.join(root.split('/')[1:])
            sub_dir_file = sub_dir + '/' + file
            dir_dic[sub_dir_file] = root + '/' + file

    for root, dirs, files in os.walk(d2):
        for file in files:
            sub_dir = '/'.join(root.split('/')[1:])
            sub_dir_file = sub_dir + '/' + file
            full_dir_file = root + '/' + file
            if sub_dir_file in dir_dic:
                shutil.move(full_dir_file,  dir_dic[sub_dir_file] + '_2')
            else:
                os.makedirs(d1 + '/' + sub_dir, exist_ok=True)
                shutil.move(full_dir_file, d1 + '/' + sub_dir_file)
    os.rename(d1, 'new_dir')
    shutil.rmtree(d2, ignore_errors=True)
    return

if __name__ == '__main__':
    app.run(main)
