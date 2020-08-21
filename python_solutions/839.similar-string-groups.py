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
#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
# https://leetcode.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (38.35%)
# Total Accepted:    22.9K
# Total Submissions: 59.6K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# Two strings X and Y are similar if we can swap two letters (in different
# positions) of X, so that it equals Y. Also two strings X and Y are similar if
# they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars",
# "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
# even though they are not similar.  Formally, each group is such that a word
# is in the group if and only if it is similar to at least one other word in
# the group.
#
# We are given a list A of strings.  Every string in A is an anagram of every
# other string in A.  How many groups are there?
#
#
# Example 1:
# Input: A = ["tars","rats","arts","star"]
# Output: 2
#
#
# Constraints:
#
#
# 1 <= A.length <= 2000
# 1 <= A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.
# The judging time limit has been increased for this question.
#
#
#

class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.p[px] = self.p[py] = min(px, py)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]



class Solution:
    def similar(self, x, y):
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True 

    def numSimilarGroups(self, A: List[str]) -> int:
        wordlen = len(A[0])
        A=set(A)
        divs = defaultdict(list)
        if wordlen > 6:
            for word in A:
                step = wordlen // 3
                for i in range(0, step * 3, step):
                    divs[word[i:i+step] + str(i)].append(word)
        else:
            divs['all'].extend(A)
        
        graph = defaultdict(set)
        for _list in divs.values():
            for i, a in enumerate(_list):
                for j, b in enumerate(_list[i+1:], i+1):
                    if self.similar(a, b):
                        graph[a].add(b)
                        graph[b].add(a)
        
        ans = 0 
        cc = set()
        for word in A:
            if word not in cc:
                queue = [word]
                while queue:
                    cur = queue.pop()
                    cc.add(cur)
                    for nx in graph[cur]:
                        if nx not in cc:
                            queue.append(nx)
                ans += 1
        return ans 



sol = Solution()
A = ["tars", "rats", "arts", "star"]
# A = ['abc', 'abc']
A = ["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]
A = ["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"]
print(sol.numSimilarGroups(A))
a = 'coswmccgkc'
x = tuple(a)
