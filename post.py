#!/usr/bin/env python3
from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
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
    f = open('question.rs', 'r').read().__str__().replace('pub struct Solution;', '// pub struct Solution;')
    with open(sys.argv[-1], 'w') as wh:
        wh.write(f)

os.system('/usr/local/bin/proxychains4 -q leetcode submit {}'.format(sys.argv[-1]))






