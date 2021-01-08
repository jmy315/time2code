import re
import sys

def find_phone(filename):
    pattern = '^((([0-9]{3}[\.|-| ]){2}[0-9]{4})|' + \
            '(\([0-9]{3}\) [0-9]{3}[-| ][0-9]{4}))$'
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                phone_num_list = words[2:]
                phone = ' '.join(phone_num_list)
                if re.match(pattern, phone):
                    print(phone)
    except IOError:
        print(f'Cannot open file: {filename}')
    return None


find_phone(sys.argv[1])
