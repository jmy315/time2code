import re
import sys

def find_valid_mac(filename):
    pattern = '^([0-9A-F]{2}:){5}[0-9A-F]{2}$'
    try:
        with open(filename, 'r') as f:
            f.readline() # skip header
            for line in f:
                words = line.split()
                server = words[0]
                mac = words[1]
                if re.match(pattern, mac):
                    print(f'{server} {mac}')
    except IOError:
        print(f'Cannot open file: {filename}')
    return None


find_valid_mac(sys.argv[1])

