"""
ideas:
1) will need to use awk command
2) need to redirect error mesage to stdout

"""
import subprocess

def run_shell():
    subprocess.run("awk -F',' '{if (( $3 >= 85 )) print $1 $4}' ./log.txt", shell=True)

    output = subprocess.run("his-command-does-not-exist", capture_output=True, shell=True)
    with open('error_log.txt', 'w') as f:
        f.write(output.stderr.decode('utf-8'))
    

run_shell()
