"""
idea:
1) read each line and get first and last name
2) get 1st letter of fistname and concatenate with lastname as username
3) keep a dic for used usernames, check everytime when a new username created
4) key -> value will be username -> counter 
5) write to a new file with extra column 'Username'

complexity: O(N) where N is the number of lines
"""

from absl import app

def main(argv):
    create_usernames(argv[1])
    return

def create_usernames(file):
    dic = {}
    f = open('newfile', 'w')
    with open(file, 'r') as fd:
        header = fd.readline()
        f.write(header.rstrip() + ' Username\n')
        for line in fd.readlines():
            words = line.split()
            username = (words[0][0] + words[1]).lower()
            if username in dic:
                dic[username] += 1
                username = username + str(dic[username])
            else:
                dic[username] = 1
            f.write(' '.join(words) + ' ' + username + '\n')
    f.close()

if __name__ == '__main__':
    app.run(main)




