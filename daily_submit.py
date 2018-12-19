#!/user/bin/env python
import os
import random
import subprocess
import re
from time import sleep
from shutil import copyfile


def auto_sumbit():
    file = "ac.c"
    while not file.endswith(".rb"):
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
        p = subprocess.Popen(['bash', 'login.sh'])
        try:
            p.wait(10)
        except subp.TimeoutExpired:
            p.kill()


def sleep_submit():
        # logout before login for the existence of multiple accounts
    os.system("leetcode user -L")
    while True:
        login_account()
        auto_sumbit()
        sleep(random.randint(3600 * 3, 3600 * 5))


sleep_submit()
