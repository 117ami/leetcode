#
# @lc app=leetcode id=541 lang=python
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (44.60%)
# Total Accepted:    51.2K
# Total Submissions: 114.8K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            return s
        return ''.join([s[i:i + k] if i % (2 * k) !=
                        0 else s[i:i + k][::-1] for i in range(0, len(s), k)])


s = Solution()
astr = "abcdefg"
k = 2
print(s.reverseStr(astr, k))


        """
        
