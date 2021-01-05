import sys

def most_visited_web(filename):
    web_count_dict = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                for word in words[1:]:
                    web_count_dict[word] = web_count_dict.get(word, 0) + 1
    except IOError:
        print(f'Cannot open file: {filename}')
        return None
    sorted_web_count = sorted(web_count_dict.items(), key=lambda x: x[1], reverse=True)
    last_count = 0
    for index,(key,value) in enumerate(sorted_web_count):
        if index < 5 or value == last_count:
            print(f'{key}: {value}')
            last_count = value

most_visited_web(sys.argv[1])
