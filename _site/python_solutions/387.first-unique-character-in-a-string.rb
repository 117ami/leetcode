#
# @lc app=leetcode id=387 lang=ruby
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (48.34%)
# Total Accepted:    211.6K
# Total Submissions: 435.5K
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#
# @param {String} s
# @return {Integer}

def first_uniq_char(s)
  ('a'..'z').map { |c| [s.index(c), s.rindex(c)] }.select { |i, j| i && i == j }.map(&:first).min || -1
end

def first_uniq_char2(s)
  counter = s.chars.group_by(&:itself)
  s.each_char.with_index do |c, i|
    return i if counter[c].size == 1
  end
  -1
end

s = 'looveleetcode'
s = 'aaa'
p first_uniq_char(s)
p s.rindex('o')
