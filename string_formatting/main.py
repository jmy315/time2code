"""
idea
1) use for loop to deal with num from 1 to n
2) use python default func to convert the number

complexity: O(N) where N is input number
"""
from absl import app

def main(argv):
    string_format(argv[1])

def string_format(d_str):
    if not d_str.isdigit():
        return False
    d = int(d_str)
    for i in range(1, d+1):
        print('{0:2d} {0:3o} {0:2x} {0:7b}'.format(i))
    return True


if __name__ == '__main__':
    app.run(main)
