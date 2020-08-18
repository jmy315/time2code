from absl import app

def main(argv):
    pangrams(argv[1])

def pangrams(file):
    with open(file, 'r') as fd:
        for line in fd:
            alpha = set(''.join(line.split()))
            if len(alpha) >= 26:
                print('pangram')
            else:
                print('not pangram')
    return

if __name__ == '__main__':
    app.run(main)
