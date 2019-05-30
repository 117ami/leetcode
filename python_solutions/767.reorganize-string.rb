#
# @lc app=leetcode id=767 lang=ruby
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (42.02%)
# Total Accepted:    26.5K
# Total Submissions: 62.8K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty
# string.
#
# Example 1:
#
#
# Input: S = "aab"
# Output: "aba"
#
#
# Example 2:
#
#
# Input: S = "aaab"
# Output: ""
#
#
# Note:
#
#
# S will consist of lowercase letters and have length in range [1, 500].
#
#
#
#
#
# @param {String} s
# @return {String}
def reorganize_string(s)
  cs = s.chars.group_by(&:itself).values.sort_by(&:size).flatten
  i = 0
  res = []
  until cs.empty?
    res[i] = cs.pop
    return "" if i > 0 && i < s.size - 1 && (res[i] == res[i - 1] || res[i] == res[i + 1])

    i += 2
    i = 1 if i >= s.size
  end
  res.join
end

s = 'bbcacacbcbcb'
s = "aab"
p reorganize_string(s)
