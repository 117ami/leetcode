#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (48.82%)
# Total Accepted:    3.1K
# Total Submissions: 6.4K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
# concatenated with itself 1 or more times)
#
# Return the largest string X such that X divides str1 and X divides str2.
#
#
#
# Example 1:
#
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
# Example 2:
#
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
# Example 3:
#
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
#
#
# Note:
#
#
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.
#
#
import math


class Solution:
    def divide(self, s, m):
        return all(s[i] == s[i % m] for i in range(len(s)))

    def gcdOfStrings(self, s1, s2):
        z = math.gcd(len(s1), len(s2))
        if self.divide(s1, z) and self.divide(s2, z) and s1[0:z] == s2[0:z]:
            return s1[0:z]
        return ""


s = Solution()
print(s.gcdOfStrings("ABABAB", "ABAB"))
