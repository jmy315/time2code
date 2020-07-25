"""
idea:
1) read each line and get the number (int/float)
2) if number > 85, add server name and percentage to a list
3) print the list

Complexity: O(N) where N is # of lines 
"""


from absl import app

def main(argv):
    find_disk_full(argv[1])
    return

def find_disk_full(file):
    li = []
    with open(file, 'r') as fd:
        for line in fd:
            words = line.split()
            num = float(words[-1].rstrip('%'))
            if num > 85:
                if num.is_integer():
                    li.append(words[0] + ', ' + str(int(num)) + '%')
                else:
                    li.append(words[0] + ', ' + str(num) + '%')
    for i in li:
        print(i)
    return


if __name__ == '__main__':
    app.run(main)
