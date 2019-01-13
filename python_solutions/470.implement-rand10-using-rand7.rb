#
# @lc app=leetcode id=470 lang=ruby
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (44.03%)
# Total Accepted:    5.6K
# Total Submissions: 12.7K
# Testcase Example:  '1'
#
# Given a function rand7 which generates a uniform random integer in the range
# 1 to 7, write a function rand10 which generates a uniform random integer in
# the range 1 to 10.
#
# Do NOT use system's Math.random().
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: 1
# Output: [7]
#
#
#
# Example 2:
#
#
# Input: 2
# Output: [8,4]
#
#
#
# Example 3:
#
#
# Input: 3
# Output: [8,1,10]
#
#
#
#
# Note:
#
#
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is
# called.
#
#
#
#
# Follow up:
#
#
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
#
#
#
#
#
# The rand7() API is already defined for you.
# def rand7()
# @return {Integer} a random integer in the range 1 to 7

def rand10
  loop do
    r = 7 * (rand7 - 1) + rand7
    return r % 10 + 1 if r <= 40
  end
end
