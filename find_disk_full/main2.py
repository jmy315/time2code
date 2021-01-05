import sys

def find_disk_full(filename):
    server_dict = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                server = words[0]
                usage = float(words[-1][:-1])
                if usage > 85:
                    server_dict[server] = usage
    except IOError:
        print(f'Cannot open file: {filename}')
        return None
    for key,value in server_dict.items():
        print(f'{key}, {value:.1f}%')
    return None



find_disk_full(sys.argv[1])
