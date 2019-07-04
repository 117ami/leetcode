# coding: utf-8
"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab". 
Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
Note:
The length of A and B will be between 1 and 10000.

"""

from collections import Counter


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not set(B).issubset(set(A)):
            return -1
        s = A
        i = 1
        while len(s) < max([len(B) * 3, len(A) * 2]):
            if B in s: return i
            s, i = s + A, i + 1
        return -1


A = "abcd"
B = "cdabcdab"

print(Solution().repeatedStringMatch(A, B))

print(set(B))
