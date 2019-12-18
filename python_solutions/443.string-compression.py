#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Easy (39.19%)
# Total Accepted:    78.1K
# Total Submissions: 199.3K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters, compress it in-place.
# 
# The length after compression must always be smaller than or equal to the
# original array.
# 
# Every element of the array should be a character (not int) of length 1.
# 
# After you are done modifying the input array in-place, return the new length
# of the array.
# 
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# 
# Example 1:
# 
# 
# Input:
# ["a","a","b","b","c","c","c"]
# 
# Output:
# Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# 
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by
# "c3".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# ["a"]
# 
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# 
# Explanation:
# Nothing is replaced.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# Output:
# Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# 
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb"
# is replaced by "b12".
# Notice each digit has it's own entry in the array.
# 
# 
# 
# 
# Note:
# 
# 
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
# 
# 
#
import collections
class Solution:
    def compress(self, chars):
        left = cter = 0
        pre = chars[0]
        for i, e in enumerate(chars):
            if i == 0 or pre == e:
                cter += 1
            if pre != e:
                chars[left] = pre
                left += 1
                pre = e 
                if cter > 1:
                    for x in list(str(cter)):
                        chars[left] = x
                        left += 1
                cter = 1

        chars[left] = pre
        left += 1
        if cter > 1: 
            for x in list(str(cter)): 
                chars[left] = x 
                left += 1
                
        return left

s = Solution()
chars = ["a", "a","b","b","b","b","b","b","b","b","b","b","b","b"]
# chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
chars = ["a","a","a","b","b","a","a"]
print(s.compress(chars))


