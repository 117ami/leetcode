# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
from typing import List
from collections import OrderedDict
from bisect import bisect_left


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.removed = set()
        self.uni = OrderedDict()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return next(iter(self.uni)) if self.uni else -1

    def add(self, value: int) -> None:
        if value in self.removed:
            return
        if value in self.uni:
            self.uni.pop(value)
            self.removed.add(value)
        else:
            self.uni[value] = True


# Your FirstUnique object will be instantiated and called as such:
nums = [2, 2, 3, 5]
obj = FirstUnique(nums)
print(obj.showFirstUnique())
obj.add(2)
obj.add(5)
print(obj.showFirstUnique())

od = OrderedDict()
od[9] = 10
od[1] = 2
print(od)
print(next(iter(od)))
