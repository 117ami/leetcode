#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#
# algorithms
# Medium (56.58%)
# Total Accepted:    12.5K
# Total Submissions: 22.1K
# Testcase Example:  '"abcd"\n2'
#
# Given a string s, a k duplicate removal consists of choosing k adjacent and
# equal letters from s and removing them causing the left and the right side of
# the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made.
#
# It is guaranteed that the answer is unique.
#
#
# Example 1:
#
#
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
#
# Example 2:
#
#
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
#
# Example 3:
#
#
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.
#
#
#


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [''] * len(s)
        i = 0
        for c in s:
            if i == 0 or c != stack[i - 1][0]:
                stack[i] = (c, 1)
            elif c == stack[i - 1][0]:
                if stack[i - 1][1] == k - 1:
                    i -= k
                else:
                    stack[i] = (c, stack[i - 1][1] + 1)
            i += 1
        #     print(i, stack)
        # print(i)
        return ''.join([a[0] for a in stack[:i]])


s = Solution()
ss, k = "pbbcggttciiippooaais", 2
# ss, k = "deeedbbcccbdaa", 3
# ss, k = "abcd", 2
print(s.removeDuplicates(ss, k))
