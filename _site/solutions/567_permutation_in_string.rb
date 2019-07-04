# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
#
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
# Note:
#
#     The input strings only contain lower case letters.
#     The length of both given strings is in range [1, 10,000].
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_inclusion(s1, s2)
  occ = Hash.new(0).tap { |h| s1.chars { |c| h[c] += 1 } }
  i = 0
  tmp = occ.dup
  s2.each_char.with_index do |c, j|
    unless occ.key?(c)
      i = j + 1
      tmp = occ.dup
      next
    end

    while !tmp.key?(c) && i < j
      tmp[s2[i]] += 1
      i += 1
    end
    tmp[c] -= 1
    tmp.delete(c) if tmp[c].zero?
    return true if tmp.empty?
  end
  false
end

s1 = 'adc'
s2 = 'dcda'
p check_inclusion(s1, s2)
