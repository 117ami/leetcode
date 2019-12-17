#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (60.59%)
# Total Accepted:    260.7K
# Total Submissions: 430.2K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
#
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
#
#
#


class Solution:
    def fizzBuzz(self, n):
        res = [''] * n
        for i in range(1, n + 1):
            if i % 15 == 0:
                res[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                res[i - 1] = 'Fizz'
            elif i % 5 == 0:
                res[i - 1] = 'Buzz'
            else:
                res[i - 1] = str(i)
        return res


s = Solution()
print(s.fizzBuzz(15))
