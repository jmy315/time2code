"""
idea:
1) read the file and count the total games
2) read each line and find location of 'ABC' and its score
3) create a list to store True/False for win/lose
4) calculate the win rate 
5) find the largest subset that has the most True

complexity: O(N) where N is number of games
"""

import sys

def win_rate(filename):
    total = 0
    win_list = []
    with open(filename, 'r') as f:
        f.readline()
        lines = f.readlines()
        total = len(lines)
        for line in lines:
            words = line.split()
            scores =  words[2].split('-')
            if words[0] == 'ABC':
                if int(scores[0]) > int(scores[1]):
                    win_list.append(True)
                else:
                    win_list.append(False)
            else:
                if int(scores[0]) < int(scores[1]):
                    win_list.append(True)
                else:
                    win_list.append(False)
    total_win = 0
    streak = 0
    longest = 0
    last_game = False
    for result in win_list:
        if result:
            total_win += 1
            if last_game:
                streak += 1
            else:
                streak = 1
                last_game = True
        else:
            if streak > longest:
                longest = streak
            streak = 0
            last_game = False

    print('Win rate: {:.1f}%'.format(100*total_win/total))
    if longest < streak:
        longest = streak
    print('Longest winning streak: {}'.format(longest))
    return

win_rate(sys.argv[1])
