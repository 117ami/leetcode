#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.47%)
# Total Accepted:    42.6K
# Total Submissions: 89.5K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
#
# Note:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#
#
#


class Solution:
    def helper(self, a, b):
        for i in range(len(a) - self.maxlen):
            j, k, curlen = i, 0, 0 
            while j < len(a) and k < len(b):
                if a[j] == b[k]:
                    curlen += 1
                    self.maxlen = max(self.maxlen, curlen)
                else:
                    curlen = 0
                j += 1
                k += 1
        
    # solution 2: check one by one 
    def findLength2(self, a, b):
        self.maxlen = 0
        self.helper(a, b)
        self.helper(b, a)
        return self.maxlen
    
    # solution 1: dynamic programming
    def findLength1(self, a, b):
        dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
        res = 0
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        
        return res 
    
    # solution 3 : binary search 
    def findLength(self, a, b):
        def check(length): # O(n^2)
            seen = {a[i:i + length] # array slicing is O(n)
                    for i in range(len(a) - length + 1)}
            return any(b[j:j + length] in seen
                       for j in range(len(b) - length + 1))
    
        a = ''.join(map(chr, a))
        b = ''.join(map(chr, b))
        lo, hi = 0, min(len(a), len(b)) + 1
        
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi - 1
                
        return lo - 1   


a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4, 7]
a, b = [1,0,0,0,0], [0,0,0,0,1]
s = Solution()
print(s.findLength(a, b))
