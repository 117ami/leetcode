#
# @lc app=leetcode id=316 lang=ruby
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (31.54%)
# Total Accepted:    51.3K
# Total Submissions: 161.8K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
# Example 1:
#
#
# Input: "bcabc"
# Output: "abc"
#
#
# Example 2:
#
#
# Input: "cbacdcbc"
# Output: "acdb"
#
#
# @param {String} s
# @return {String}
def remove_duplicate_letters(s)
  letters = s.chars.uniq.sort
  letters.each do |l|
    return l + remove_duplicate_letters(s[s.index(l)..-1].gsub(l, '')) if s[s.index(l)..-1].chars.uniq.sort == letters
  end
  ''
end

s = 'cbacdcbc'
s = 'bcabc'
p remove_duplicate_letters(s)
