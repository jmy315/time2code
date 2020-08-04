"""
idea:
1) list all files under given dir
2) for reach file, check for dir, .txt, .html, .jpg
3) for dir, only check for name 'pictures', and move .jpg files into it
4) for .html, rename them to .htm 
5) for .txt, create a new file 'stuff.txt' and read all .txt and write to 'stuff.txt'

complexity: O(NlogN) where N is number of files
"""
from absl import app
import os

def main(argv):
    file_mani(argv[1])

def file_mani(dir):
    if not os.path.isdir(dir):
        return False
    files = os.listdir(dir)
    text_files = []
    for i in files:
        if i == 'pictures':
            if not os.path.isdir(dir + '/' + i):
                return False
        elif i.split('.')[-1] == 'jpg':
            os.rename(dir + '/' + i, dir + '/pictures/' + i)
        elif i.split('.')[-1] == 'txt':
            text_files.append(i)
        elif i.split('.')[-1] == 'html':
            os.rename(dir + '/' + i, dir + '/' + i[:-1])
    text_files = sorted(text_files)
    with open(dir + '/stuff.txt', 'w') as fd:
        for t in text_files:
            with open(dir + '/' + t, 'r') as f:
                fd.write(f.read())
    return True

if __name__ == '__main__':
    app.run(main)





