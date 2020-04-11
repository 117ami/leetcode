from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#
# https://leetcode.com/problems/k-similar-strings/description/
#
# algorithms
# Hard (37.66%)
# Total Accepted:    14.2K
# Total Submissions: 37.8K
# Testcase Example:  '"ab"\n"ba"'
#
# Strings A and B are K-similar (for some non-negative integer K) if we can
# swap the positions of two letters in A exactly K times so that the resulting
# string equals B.
# 
# Given two anagrams A and B, return the smallest K for which A and B are
# K-similar.
# 
# Example 1:
# 
# 
# Input: A = "ab", B = "ba"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "abc", B = "bca"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "abac", B = "baca"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aabc", B = "abca"
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length == B.length <= 20
# A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e',
# 'f'}
# 
# 
#
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        z = [e for e in zip(A, B) if e[0] != e[1]]
        seen = defaultdict(list)
        res = 0
        print(z)
        
        for i, t in enumerate(z):
            rt = (t[1],t[0])
            if rt in seen:
                res += 1
                z[seen[rt][-1]] = '#'
                z[i] = '#'
                seen[rt].pop()
                if len(seen[rt])==0:
                    del seen[rt]
            else:
                seen[t].append(i)

        z = [e for e in z if e !='#']
        print(z)
        m = [0]*6
        pre_k = 0
        for k, e in enumerate(z):
            i, j = ord(e[0])-97, ord(e[1])-97
            m[i] +=1 
            m[j]-=1 
            if all(n == 0 for n in m): 
                res += k - pre_k
                pre_k = k +1
        return res 

                    
sol = Solution()
a = "abcd"
b = "badc"
a, b = "ab", 'ba'
a, b ='aabc', 'abca'
a, b = "aabbccddee","dcacbedbae"
print(list(zip(a, b)))
print(sol.kSimilarity(a, b))

