"""
idea:
1) handle open file error in case file does not exist
2) handle type error in case given line does have numbers
3) handle division by zero error

Complexity: O(N) where N is number of lines
"""

import sys

def division(filename):
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                nums = line.split()
                if len(nums) < 2:
                    print('Error: Too few numbers given')
                    continue
                try:
                    result = float(nums[0]) / float(nums[1])
                    print(result)
                except ValueError:
                    print('Error: line contains non digits')
                except ZeroDivisionError:
                    print('Error: division by 0')
    except IOError:
        print('Error: file does not exist')
        return False



division(sys.argv[1])
