from absl import app

def main(argv):
    grouped(argv[1])

def grouped(file):
    li = []
    with open(file, 'r') as fd:
        for line in fd:
            li.append(line.split())
    newli = sorted(li, key=lambda i: i[1])
    with open("newfile", 'w') as fd:
        #for i in newli:
         #   fd.write(' '.join(i) + '\n')
        fd.writelines([' '.join(line) + '\n' for line in newli] )
    return

if __name__ == '__main__':
    app.run(main)
