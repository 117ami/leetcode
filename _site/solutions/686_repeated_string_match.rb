
# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
# Note:
# The length of A and B will be between 1 and 10000.
#

# @param {String} a
# @param {String} b
# @return {Integer}
require 'set'
def repeated_string_match(a, b)
  return -1 unless Set.new(b.chars).subset?(Set.new(a.chars))
  s = a
  i = 1
  while s.length < [a.size * 2, b.size * 3].max
    return i if s.include?(b)
    s += a
    i += 1
  end
  -1
end

a = 'abcd'
b = 'cdabcdab'
p repeated_string_match(a, b)
