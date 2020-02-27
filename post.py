#!/usr/local/bin/python3
import sys 
import os  

if len(sys.argv) == 2 or sys.argv[1] == "xiu":
    print("🐬🐬🐬 Submint through account : XIU")
    os.system("cp /Users/alpha/.lc/xiu.json /Users/alpha/.lc/leetcode/user.json")
elif sys.argv[1] == '117':
    print("🔥🔥🔥 Submint through account : 117")
    os.system("cp /Users/alpha/.lc/firefly.json /Users/alpha/.lc/leetcode/user.json")
else:
    print("Either xiu or 117")
    exit(0)

if sys.argv[-1].endswith('rs'):
    print("Submitting Rust solution")
    f = open('question.rs', 'r').read().__str__().replace('pub struct ', '// pub struct')
    with open(sys.argv[-1], 'w') as wh:
        wh.write(f)

os.system('/usr/local/bin/proxychains4 -q leetcode submit {}'.format(sys.argv[-1]))


