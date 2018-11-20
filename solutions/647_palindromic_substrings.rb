#
# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.
#

# @param {String} s
# @return {Integer}
def count_substrings(s)
  return s.length if s.length <= 1
  @counter = 0
  0.upto(s.length - 1).each do |i|
    expand_palind(s, i, i)
    expand_palind(s, i, i + 1)
  end
  @counter
end

def expand_palind(s, i, j)
  while i >= 0 && j < s.length && s[i] == s[j]
    @counter += 1
    i -= 1
    j += 1
  end
end

s = 'aaa'
p count_substrings(s)
