"""
idea:
1) create a OrderedDict [character -> max_count]
2) traverse the string, use temp to store each character and keep a counter
3) keep going until a new character is seen, store the temp and counter to dict

complexity: O(NlogN) as N is the number of characters in the string
"""

from collections import OrderedDict

def con_occur(s):
    dic = OrderedDict()
    cur = s[0]
    count = 1
    for c in s[1:]:
        if cur != c:
            if cur not in dic or dic[cur] < count:
                dic[cur] = count
            cur = c
            count = 1
        else:
            count += 1
    sorted_c = sorted(dic.items(), key=lambda i:i[1], reverse=True)
    for k, v in sorted_c[:3]:
        print(k + ',' + str(v))
    return

con_occur('aaabbccaddde')
