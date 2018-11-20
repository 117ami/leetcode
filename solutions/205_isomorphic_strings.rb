# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
  return false unless s.length == t.length
  ms = []
  mt = []
  s.each_char.with_index do |c, i|
    return false if ms[c.ord] != mt[t[i].ord]
    ms[c.ord] = mt[t[i].ord] = i
  end
  true
end

s = 'paper'
t = 'title'
p is_isomorphic(s, t)
