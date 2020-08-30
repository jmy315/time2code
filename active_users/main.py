"""
idea: 
1) scan fileB and save active usernames in a list
2) scan fileA for each active usernames, if found and email is @yaboo.com, print out the username and phone number
3) if not found, printer username and default phone number

complexity: O(max(M,N)) where M is the number of lines in fileA and N is number of lines in fileB
"""

from absl import app

def main(argv):
    active_users(argv[1], argv[2])

def active_users(file1, file2):
    users = set()
    with open(file2, 'r') as f2:
        f2.readline()
        for line in f2:
            words = line.split()
            if words[1] == 'Yes':
                users.add(words[0])
    with open(file1, 'r') as f1:
        for line in f1:
            words = line.split()
            email_parts = words[0].split('@')
            username = email_parts[0]
            domain = email_parts[1]
            if username in users and domain.split('.')[0] == 'yaboo':
                print('{} {} {}'.format(username, words[1], words[2]))
                users.remove(username)
    for leftover in users:                
        print('{} {}'.format(leftover, '(444) 123-1233'))
    return

if __name__ == '__main__':
    app.run(main)
