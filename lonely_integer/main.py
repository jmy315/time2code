"""
idea:
1) create a dict {num -> True/False}
2) True means occurring once
3) False means occuring twice or not exist
4) print out the dict key that is True

complexity: O(N) where N is number of items in the list
"""

from absl import app

def main(argv):
    del argv
    lonely_integer([1,1,2])
    lonely_integer([0,0,1,2,1])

def lonely_integer(list):
    dic = {}
    for i in list:
        if i in dic:
            dic[i] = False
        else:
            dic[i] =  True
    for k,v in dic.items():
        if v:
            print(k)
            return
    return

if __name__ =='__main__':
    app.run(main)
