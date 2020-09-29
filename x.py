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
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007

arr = [[1,10,30,2,1],[2,10,35,6,3],[3,10,40,6,0],[4,10,50,8,10],[5,10,60,10,9],[6,10,65,0,0],[7,30,35,9,10],[8,30,40,1,0],[9,30,50,9,2],[10,30,60,9,8],[11,30,65,0,1],[12,35,40,5,8],[13,35,50,9,1],[14,35,60,4,0],[15,35,65,1,1],[16,40,50,8,5],[17,40,60,7,4],[18,40,65,2,7],[19,50,60,0,10],[20,50,65,6,7],[21,60,65,8,5],[22,15,20,4,9],[23,15,25,8,8],[24,15,45,7,1],[25,15,55,6,0],[26,20,25,5,0],[27,20,45,6,0],[28,20,55,8,8],[29,25,45,9,10],[30,25,55,4,6],[31,45,55,8,0]]
for a in arr:
    i, j, k, m, n = a
    print(f"insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('{i}', '{j}', '{k}', '{m}', '{n}');")
sol = Solution()


