#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#
# https://leetcode.com/problems/iterator-for-combination/description/
#
# algorithms
# Medium (63.51%)
# Total Accepted:    2.1K
# Total Submissions: 3.3K
# Testcase Example:  '["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]\r' +
#   '\n[["abc",2],[],[],[],[],[],[]]\r'
#
# Design an Iterator class, which has:
#
#
# A constructor that takes a string characters of sorted distinct lowercase
# English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length
# combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next
# combination.
#
#
#
#
# Example:
#
#
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates
# the iterator.
#
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
#
#
#
# Constraints:
#
#
# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.
#
#
#
import itertools


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                yield from combinations(cur, i + 1)
                cur.pop()

        self.combos = combinations([], 0)
        self.current = True
        self.hasNextCalled = False

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
for i in range(10):
    if obj.hasNext():
        print(i, obj.next())

# g = itertools.combinations('aabc', 2)
# print(list(g))

# from aux import perms
# for i in perms('aabc',2):
#     print(i)
