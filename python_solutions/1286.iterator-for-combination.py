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
        # self.cter = 1
        # n = len(characters)
        # for i in range(1, combinationLength + 1):
        #     self.cter = self.cter * (n - i + 1) / i
        # self.cter = int(self.cter)
        self.cter = 0
        self.perm = sorted(itertools.combinations(characters, combinationLength))
        # print(self.perm)

    def next(self) -> str:
        v = self.perm[self.cter]
        self.cter += 1
        return ''.join(v)

    def hasNext(self) -> bool:
        return self.cter < len(self.perm)
        


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

