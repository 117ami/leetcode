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

    os.system("leetcode submit " + nfname)
    os.remove(nfname)


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
    os.system("leetcode user -L")
    while True:
        try:
            login_account()
            auto_sumbit()
            sleep(random.randint(3600 * 3, 3600 * 5))
        except BaseException:
            pass


sleep_submit()
