#!/user/bin/python3
import os, sys
import random
import subprocess
import re
from time import sleep
from shutil import copyfile
from telegm import ServerLogger


def sumbit_solution():
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
    ServerLogger().alertGreco(str(nfname) + ' submitted for agl' )
    os.remove(nfname)
    return 'expired' in str(res.stdout)


def is_login():
    ''' check whether user is on board.'''
    return not ("ERROR" in str(subprocess.Popen(
        ["leetcode", "user"], stdout=subprocess.PIPE).communicate()[0]))


def login():
    os.system('ruby login.rb')


if __name__ == '__main__':
    print('isLogin:', is_login())
    while True:
        try:
            if sumbit_solution():
                login()
            # sleep(random.randint(500, 1200))
            sleep(10800)
        except Exception as e:
            print(e)




s = Solution()


