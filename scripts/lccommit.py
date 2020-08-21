import sys, os, time, json
import subprocess 

if __name__ == "__main__":
    title, diff = sys.argv[1:3]
    tid = title.split('/')[-1].split('.')[0]
    files = subprocess.check_output("find python_solutions/ -type f -name {}*".format(tid), shell=True).decode('utf8').split('\n')
    files = [f for f in files if f]
    print(files)
  
