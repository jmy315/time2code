"""
idea
1) read the input and store them into a deque
2) for deque is not empty, check head and tail, pop the bigger one
        check if the popped num is greater than the previous popped number
            if so, output No
            else, continue
3) once deque is empty and everything checks out, output YES

complexity: O(N) where N is total number of cubes
"""
from absl import app
from collections import deque

def main(argv):
    piling_up(argv[1])

def piling_up(file):
    with open(file, 'r') as fd:
        num_of_runs = int(fd.readline().strip())
        for _ in range(num_of_runs):
            num_of_cubes = int(fd.readline().strip())
            cubes = deque([int(i) for i in fd.readline().split()])
            max = 2**31
            failed = False
            while cubes:
                new_cube = 0
                
                # pop the larger cube
                if cubes[0] > cubes[-1]:
                    new_cube = cubes.popleft()
                else:
                    new_cube = cubes.pop()

                # compare to the previous popped cube
                if new_cube > max:
                    failed = True
                    break

                # update the popped cube
                max = new_cube
            if failed:
                print('NO')
            else:
                print('YES')
    return

if __name__ == '__main__':
    app.run(main)
            
