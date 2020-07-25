from absl import app

def main(argv):
    print(count_lines(argv[1]))

def count_lines(file):
    counter = 0
    with open(file, 'r') as fd:
        for line in fd:
            # strip leading and ending spaces
            words = line.strip()
            if words  == '':
                continue
            if words[0] == '^' and words[-1] == '$':
                c = 0
                for v in words:
                    # checks if number of '^' and '$' are the same
                    # we don't care about how many are there
                    if v == '^':
                        c += 1
                    if v == '$':
                        c -= 1
                if c == 0:
                    continue
            counter += 1
    return counter

if __name__ == '__main__':
    app.run(main)
            
