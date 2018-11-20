# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# @param {String} s
# @return {Integer}
def longest_palindrome(s)
  lens = s.chars.group_by(&:itself).values.map(&:size)
  r = lens.map { |v| v.odd? ? v - 1 : v }.reduce(:+)
  r += 1 unless r == lens.reduce(:+)
  r
end

s = 'abccccddA'
s = 'aabAAb'
p longest_palindrome(s)
