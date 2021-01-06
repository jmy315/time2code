import re
import sys

def find_valid_ips(filename):
    pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}' \
            + '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'    
    try:
        with open(filename, 'r') as f:
            for line in f:
                if re.match(pattern, line):
                    print(line, end='')
    except IOError:
        print(f'Cannot open file: {filename}')
    return None

find_valid_ips(sys.argv[1])
