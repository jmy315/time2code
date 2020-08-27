"""
idea:
1) read the file and get num of lines
2) make sure input N is non-negative int
3) compare N and num of lines, if N is bigger, just print the whole file
4) if N is smaller, print the last N lines

complexity: O(n) where n is number of lines
"""

from absl import app

def main(argv):
    last_n_lines(argv[1], argv[2])

def last_n_lines(file, N):
    if not N.isdigit():
        print('N is not an non-negative integer')
        return
    with open(file, 'r') as f:
        lines = f.read()
        
        # it takes care of N greater than len 
        print(''.join(lines[-int(N):]))
    return


if __name__ == '__main__':
    app.run(main)
