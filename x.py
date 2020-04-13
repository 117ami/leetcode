from collections import Counter
from bisect import insort
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            a, b = stones.pop(), stones.pop()
            if a > b:
                insort(stones, a - b)
        return stones[0]


s = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeight(s))
