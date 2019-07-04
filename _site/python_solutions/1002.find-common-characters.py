#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (67.79%)
# Total Accepted:    11.9K
# Total Submissions: 17.6K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
#
# You may return the answer in any order.
#
#
#
#
# Example 1:
#
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
#
#
#
# Example 2:
#
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
#
#
#
#


class Solution:
    def commonChars(self, a):
        res = [[c] * min([w.count(c) for w in a]) for c in set(a[0])]
        return [i for e in res for i in e]


# a = ["cool","lock","cook"]
a = ["bella", "label", "roller"]
print(Solution().commonChars(a))
