from collections import Counter
from bisect import insort
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        carry = (sum(sh if d == 1 else -sh for d,
                     sh in shift) + len(s)) % len(s)
        print(carry)
        return s[-carry:] + s[:-carry]


s = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
print(Solution().stringShift(s, shift))
