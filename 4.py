from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left as bl, bisect_right as br 
from functools import reduce, lru_cache 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f

class Solution:
    def minTaps(self, n: int, ranges):
        x = [[i - j, i + j] for i, j in enumerate(ranges)]
        x.sort(key=lambda e: (e[1], e[0]))
        # print(x)
        stack = []
        for e in x:
            if e[0] == e[1]: continue
            if not stack:
                stack.append([max(0, e[0]), e[1]])
            else:
                if stack and stack[-1] == [0, n]: 
                    return 1
                # print(e, stack)
                if e[1] == stack[-1][1]: continue 
                while stack and e[0] <= stack[-1][0]:
                    stack.pop()
                stack.append([max(0, e[0]), e[1]])
        
        print(stack)
        x = []
        for i, j in stack[::-1]:
            if not x: x.append([i, j])
            else:
                while x and j >= x[-1][0]:
                    tmp = x.pop()
                x.append(tmp)
                x.append([i, j])
        print(x)
        items = {i:0 for i in range(n + 1)}
        for a, b in x:
            if a == b: continue
            for j in range(a, b+1):
                if j in items:
                    del items[j]
        
        return len(x) if len(items) == 0 else -1

        



sol = Solution()
n, ranges = 5, [3,4,1,1,0,0]
n, ranges = 68, [0,0,0,1,4,2,2,2,2,4,0,0,0,5,4,0,0,5,3,0,1,1,5,1,1,2,4,1,0,4,3,5,1,0,3,3,4,2,2,4,3,1,1,0,4,0,2,1,4,0,0,3,3,1,1,4,4,2,0,3,4,0,1,5,3,0,1,0,2]
# n, ranges = 7, [1,2,1,0,2,1,0,1]
# n, ranges = 8, [4,0,0,0,0,0,0,0,4]
# n, ranges = 9, [0,5,0,3,3,3,1,4,0,4]
# n, ranges = 3, [0,0,0,0]
# n, ranges = 8, [4,0,0,0,4,0,0,0,4]
print(sol.minTaps(n, ranges))

