import sys

def create_usernames(filename):
    known_usernames = {}
    try:
        with open(filename, 'r') as f, open('newfile2', 'w') as f2:
            header = f.readline().strip()
            f2.write(f'{header} Username\n')
            for line in f:
                words = line.split()
                first = words[0]
                last = words[1]
                username = (first[0] + last).lower()
                if username not in known_usernames:
                    known_usernames[username] = 1
                else:
                    known_usernames[username] += 1
                    username = username + str(known_usernames[username])
                f2.write(f'{line.strip()} {username}\n')
    except IOError:
        print(f'Cannot open file: {filename}')
    return None



create_usernames(sys.argv[1])
