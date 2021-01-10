import sys

def string_formatting(n):
    for i in range(1, n+1):
        print(f'{i:-6} {i:-6o} {i:-6x} {i:-6b}')

string_formatting(int(sys.argv[1]))
