"""
idea:
1) walk through the list, split each string into letter and number
2) create a dict {letter -> [number1, number2, ...]}
3) dict.items() sort the keys, then sort the list
4) combine the letters and numbers back to a list

complexity: O(NMlogM) where M*N is lenth of list
"""

def order_a_list(list):
    dic = dict()
    for i in list:
        letter = i[0]
        num = int(i[1:])
        if letter not in dic:
            dic[letter] = []
        dic[letter].append(num)
    all_stuff = sorted(dic.items(), key=lambda i:i[0])
    new_list = []
    for i in all_stuff:
        for j in sorted(i[1]):
            new_list.append(i[0] + str(j))
    return(new_list)

print(order_a_list(['a1', 'b20', 'c1', 'd5', 'a3', 'b1', 'd11', 'b3']))


        
