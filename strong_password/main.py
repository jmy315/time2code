"""
idea:
1) create four varialbes to track each requirement
2) go through the passowrd char by char
3) check all four variables and return how many more chars are needed

complexity: O(N) where N is the number of chars in password
"""

from absl import app

def main(argv):
    print(strong_password(argv[1]))

def strong_password(pw):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    n_count = 0
    l_count = 0
    u_count = 0
    s_count = 0

    for c in pw:
        if c in numbers:
            n_count += 1
        elif c in lower_case:
            l_count += 1
        elif c in upper_case:
            u_count += 1
        else:
            s_count += 1

    need = 0
    if n_count == 0:
        need += 1
    if l_count == 0:
        need += 1
    if u_count == 0:
        need += 1
    if s_count == 0:
        need += 1

    if need > 6 - len(pw):
        return need
    return 6 - len(pw)



if __name__ == '__main__':
    app.run(main)
