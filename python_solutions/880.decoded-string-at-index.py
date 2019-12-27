from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right
from functools import reduce
true = True
false = False
#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#
# https://leetcode.com/problems/decoded-string-at-index/description/
#
# algorithms
# Medium (23.75%)
# Total Accepted:    9.9K
# Total Submissions: 41.6K
# Testcase Example:  '"leet2code3"\n10'
#
# An encoded string S is given.  To find and write the decoded string to a
# tape, the encoded string is read one character at a time and the following
# steps are taken:
#
#
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit (say d), the entire current tape is
# repeatedly written d-1 more times in total.
#
#
# Now for some encoded string S, and an index K, find and return the K-th
# letter (1 indexed) in the decoded string.
#
#
#
#
# Example 1:
#
#
# Input: S = "leet2code3", K = 10
# Output: "o"
# Explanation:
# The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".
#
#
#
# Example 2:
#
#
# Input: S = "ha22", K = 5
# Output: "h"
# Explanation:
# The decoded string is "hahahaha".  The 5th letter is "h".
#
#
#
# Example 3:
#
#
# Input: S = "a2345678999999999999999", K = 1
# Output: "a"
# Explanation:
# The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter
# is "a".
#
#
#
#
# Note:
#
#
# 2 <= S.length <= 100
# S will only contain lowercase letters and digits 2 through 9.
# S starts with a letter.
# 1 <= K <= 10^9
# The decoded string is guaranteed to have less than 2^63 letters.
#
#
#
#
#
#


class Solution:
    def decodeAtIndex(self, s, k):
        size = 0
        for i, c in enumerate(s):
            if c.isalpha():
                size += 1
            else:
                size *= int(c)

        for c in reversed(s):
            k = k % size
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


s = Solution()
e, k = "leet2code3", 10
e, k = "vzpp636m8y", 2920
# k = 322
print(s.decodeAtIndex(e, k))
