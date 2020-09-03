"""
idea:
2) create RE patterns for each item
3) scan thru lines and search for each patterns and save them into a tuple, then to a list
4) sort the list by name and output to a new file

Complexity: O(NlogN) where N is number of lines
"""

import re
from absl import app

def main(argv):
    clear_mess(argv[1])

def clear_mess(file):
    contacts = []
    name_p = r'[A-Za-z]+'
    phone_p = r'(?:[0-9]{3}-){2}[0-9]{4}'
    date_p = r'(?:[0-9]{2}\/){2}[0-9]{4}'

    with open(file, 'r') as f:
        for line in f:
            name = re.search(name_p, line)
            phone = re.search(phone_p, line)
            date = re.search(date_p, line)
            contacts.append((name.group(0), phone.group(0), date.group(0)))
    
    contacts = sorted(contacts, key=lambda i:i[0])

    with open('new_file', 'w') as f:
        f.write('Username Phone_num Start_date\n')
        for contact in contacts:
            f.write(' '.join(contact) +  '\n')

if __name__ == '__main__':
    app.run(main)
