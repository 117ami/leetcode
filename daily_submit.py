#!/user/bin/python3
import os, sys
import random
import subprocess
import re
from time import sleep
from shutil import copyfile


def auto_sumbit():
    file = "ac.c"
    while not file.endswith(".rb") or not re.findall(
            r"\d+", file):  # problem ID is required
        file = random.choice(os.listdir("solutions"))
    print(file)

    nfname = re.findall(r"\d+", file)[0] + ".rb"
    target = open(nfname, "w")
    with open("solutions" + "/" + file) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("require './aux.rb'"):
                target.write(line + "\n")
    target.close()

    res = subprocess.run(["leetcode", "submit", nfname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # os.system("leetcode submit " + nfname)
    print(res.stdout)
    os.remove(nfname)
    return 'expired' in str(res.stdout)


def is_login():
    ''' check whether user is on board.'''
    return not ("ERROR" in str(subprocess.Popen(
        ["leetcode", "user"], stdout=subprocess.PIPE).communicate()[0]))


def login_account():
    while not is_login():
    	print("**Login...")
    	proc = subprocess.Popen(["ruby", "login.rb"])
    	try:
    		outs, errs = proc.communicate(timeout=10)
    	except subprocess.TimeoutExpired:
    		proc.terminate()
    		outs, errs = proc.communicate()


def sleep_submit():
    # Essential: logout before login, otherwise [SESSION EXPIRED] error will be raised
    # os.system("leetcode user -L")
    while True:
        try:
            res = auto_sumbit()
            if res:
                login_account()
            sleep(random.randint(300, 500))
        except BaseException as ex:
            print("Exception", ex)


if __name__ == '__main__':
    print(is_login())
    # auto_sumbit()
    sleep_submit()
