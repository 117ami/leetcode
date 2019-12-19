import arrow
import json
import requests
import time
import re
import math
import smtplib
import os.path as op
import sys
import subprocess
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import smtplib
import argparse
 
def yahoomail(target, subject='reminder', content="just want to say Hello"):
    SMTP_SERVER = "smtp.mail.yahoo.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "caronthibur11"
    SMTP_PASSWORD = "passport123"
    EMAIL_FROM = "caronthibur11@yahoo.com"
    EMAIL_TO = target
    def send():
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = EMAIL_FROM 
        msg['To'] = EMAIL_TO
        debuglevel = True
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # mail.set_debuglevel(debuglevel)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        print("yahoo login success")
        mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print("yahoo sent success")
        mail.quit()
    send()


def checkNewProblems():
    solved_log = json.load(open('solvedlog.json', 'r'))
    res = ""
    qs = subprocess.check_output('/usr/bin/leetcode list|head', shell=True).decode('utf8')
    for line in qs.split('\n'):
        if not line: continue 
        x = re.search(r'(🔒)?\s*(✔)?\s*\[(.*)\](.*)(Hard|Easy|Medium)', line).groups()

        # unlocked and unsolved problem 
        if x[0] is None and x[2] not in solved_log:
            res += line.lstrip() + "\n"
            solved_log[x[2]] = "yes"
    
    json.dump(solved_log, open('solvedlog.json', 'w'), indent=2)
    print(res)
    return res 


if __name__ == "__main__":
    res = checkNewProblems()
    if res:
        yahoomail('i@140714.xyz', 'NEW LEETCODE PROBLEMS', res)
        print("DONE")