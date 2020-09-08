"""
idea:
1) use os.listdir to list all files under file_dir and only check files (not directories)
2) use os.issymlink to check if a file is a link, if yes, add to a list, if not add to dict 
3) for each item in list, check if it has the same inode (use os.stat.st_ino) in the dict, if so, remove the item, if not, continue

complexity: O(N) where N is number of files
"""

from absl import app
import os

def main(argv):
    rm_soft_links(argv[1])

def rm_soft_links(dir):
    items = os.listdir(dir)
    links = []
    inodes = set()
    for item in items:
        full_path = os.getcwd() + '/' + dir + '/' + item
        if os.path.islink(full_path):
            links.append((full_path, os.stat(full_path).st_ino))
        else:
            inodes.add(os.stat(full_path).st_ino)
    for i,j in links:
        if j in inodes:
            os.remove(i)

if __name__ == '__main__':
    app.run(main)
