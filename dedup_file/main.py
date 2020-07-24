from absl import app

def main(argv):
    dedup(argv[1])

def dedup(file):
    li = []
    with open(file, 'r') as fd:
        for line in fd:
            if line not in li:
                li.append(line)
    with open('newfile', 'w') as fd:
        fd.writelines(li)
    return

if __name__ == '__main__':
    app.run(main)
