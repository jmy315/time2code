"""
ideas:
1) get the sum of whole list
2) left_sum and right_sum accumulate the partial sum
3) keep a varialbe to keep track of min_diff between left and right sum

complexity: O(N) where N is the number of items in array
"""

def split_sum_2(array):
    total = sum(array)
    left_sum = 0
    right_sum = total
    min_diff = abs(left_sum - right_sum)
    min_index = 0

    for i, num in enumerate(array):
        left_sum += num
        right_sum -= num
        if min_diff > abs(left_sum - right_sum):
            min_diff = abs(left_sum - right_sum)
        else:
            min_index = i
            break
    print(array[:min_index], array[min_index:])


split_sum_2([2,7,9,4,6,1])
split_sum_2([2,7,9,461])
