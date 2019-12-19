#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (49.92%)
# Total Accepted:    4.5K
# Total Submissions: 9K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#
class Solution:
    def sequentialDigits(self, lo, hi):
        res = []
        for k in range(1, 10):
            i = k
            j = i + 1
            while i < lo and j < 10:
                i = i * 10 + j
                j += 1

            while i >= lo and i <= hi and j <= 10:
                res.append(i)
                i = i * 10 + j 
                j += 1
                
        return sorted(res) 

s = Solution()
print(s.sequentialDigits(10, 78911))


