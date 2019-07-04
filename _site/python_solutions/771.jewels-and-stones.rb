#
# @lc app=leetcode id=771 lang=ruby
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (82.07%)
# Total Accepted:    146.8K
# Total Submissions: 178.9K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings J representing the types of stones that are jewels, and
# S representing the stones you have.  Each character in S is a type of stone
# you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
#
# Example 1:
#
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
#
# Example 2:
#
#
# Input: J = "z", S = "ZZ"
# Output: 0
#
#
# Note:
#
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
#
#
#
# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
  s.chars.select { |c| j.include?(c) }.size
end

j = 'aA'
s = 'aAAbbbb'
p num_jewels_in_stones(j, s)
