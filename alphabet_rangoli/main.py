"""
idea:
1) get the input integer n and  get a sublist of alphabets
2) matrix size will be m[2n-1][4n-3]
3) start from the middle and spread out 'a', 'b', ...

complexty: O(N^2) where N is input number
"""
from absl import app

def main(argv):
    alphabet(argv[1])

def alphabet(num):
    if not num.isdigit():
        return False
    num = int(num)
    if num < 1 or num > 26:
        return False
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    sub_alpha = []
    for i in range(num):
        sub_alpha.append(alpha[i])
    m = []
    r = 2 * num - 1
    c = 4 * num - 3
    for i in range(r):
        m.append([])
        for _ in range(c):
            m[i].append('-')
    c = int(c/2)
    r = int(r/2)
    for i in range(r+1):
        cur = i
        for j in range(num - i):
            m[r + i][c + 2*j] = sub_alpha[cur + j]
            m[r + i][c - 2*j] = sub_alpha[cur + j]
            m[r - i][c + 2*j] = sub_alpha[cur + j]
            m[r - i][c - 2*j] = sub_alpha[cur + j]
    for r in m:
        print(' '.join(r))


if __name__ == '__main__':
    app.run(main)
