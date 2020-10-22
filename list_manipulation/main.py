"""
idea:
1) simple, use list comprehension for all cases

complexity: O(N^2) for N the number of items in a list
"""

def xor_lists(a, b):
    return [i for i in a if i not in b] + [i for i in b if i not in a]

def and_lists(a, b):
    return [i for i in a if i in b]

def left_lists(a, b):
    return [i for i in a if i not in b]

a = [1, 2, 3]
b = [2, 4, 6]

print(xor_lists(a, b))
print(and_lists(a, b))
print(left_lists(a, b))
