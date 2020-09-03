#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (34.00%)
# Total Accepted:    8.7K
# Total Submissions: 25.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#
#
# Note:
#
#
# A.length == 4
# 0 <= A[i] <= 9
#
#
#
#


from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, a):
        a.sort(reverse=True)
        # for u, v, s, t in perms(a):
        for u, v, s, t in permutations(a):
            # print([u,v,s,t])
            if u * 10 + v < 24 and s * 10 + t <= 59:
                return "{}{}:{}{}".format(u, v, s, t)
        return ""



# s = Solution()
# arr = [1, 2, 4, 3]
# arr = [1, 9, 6, 0]
# arr = [1, 2, 3]
# res = myperm(arr,2)
# print(list(res))

# print(s.largestTimeFromDigits(arr))
