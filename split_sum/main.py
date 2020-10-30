"""
idea:
1) get the sume of the array
2) traverse the array and accumulate the partial sum
3) while going thru, compare partial sum and check if it's half of sum
4) if so, return the splited arrays, if not, keep going

complexity: O(N) where N is number of length of array
"""

def split_sum(array):
    if len(array) <= 1:
        return False
    total = sum(array)
    cur_sum = 0
    for i, num in enumerate(array):
        cur_sum += num
        if cur_sum == total / 2:
            print(array[:i+1], array[i+1:])
            return True
    return False


split_sum([4, 6, 8, 2])
