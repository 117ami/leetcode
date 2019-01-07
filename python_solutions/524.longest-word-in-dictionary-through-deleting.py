#
# @lc app=leetcode id=524 lang=python
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (44.56%)
# Total Accepted:    34.9K
# Total Submissions: 78.3K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
#
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
#
#
#
#
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
#
#
#
# Note:
#
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
#
#
#


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for t in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in t):
                return t
        return ''


s = "abpcplea"
d = ["ale", "apple", "monkey", "plea", "blue"]
print(Solution().findLongestWord(s, d))
