import re
import sys

def hex_color_code(filename):
    pattern = '#(?:[0-9a-fA-F]{3}){1,2}'
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                matches = re.findall(pattern, line)
                for color in matches:
                    print(color)
    except IOError:
        print(f'Cannot open file: {filename}')
    return None


hex_color_code(sys.argv[1])
