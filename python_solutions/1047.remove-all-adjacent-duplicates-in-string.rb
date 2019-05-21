#
# @lc app=leetcode id=1047 lang=ruby
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (60.39%)
# Total Accepted:    4.9K
# Total Submissions: 8.1K
# Testcase Example:  '"abbaca"'
#
# Given a string S of lowercase letters, a duplicate removal consists of
# choosing two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.  It
# is guaranteed the answer is unique.
#
#
#
# Example 1:
#
#
# Input: "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
#
#
#
#
# Note:
#
#
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.
#
#
# @param {String} s
# @return {String}
def remove_duplicates(s)
  res = s.dup
  i = -1
  s.each_char do |c|
    if (i >= 0) && (res[i] == c)
      i -= 1
    else
      i += 1
      res[i] = c
    end
  end
  return '' if i == -1
  res[0..i]
end

p remove_duplicates('aaaaaaaa')
