# We are given two arrays A and B of words. Each word is a string of lowercase letters.
# Now, say thatword b is a subset of word aif every letter in b occurs in a, including multiplicity. For example, "wrr" is a subset of "warrior", but is not a subset of "world".
# Now say a word a from A is universal if for every b in B, bis a subset of a.
# Return a list of all universal words in A. You can return the words in any order.
#
# Example 1:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# Example 3:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# Example 4:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# Example 5:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
#
# Note:
#   1 <= A.length, B.length <= 10000
#   1 <= A[i].length, B[i].length<= 10
#   A[i] and B[i] consist only of lowercase letters.
#   All words in A[i] are unique: there isn't i != j with A[i] == A[j].
#
#  https://leetcode.com/problems/word-subsets/description/
require './aux.rb'

# @param {String[]} a
# @param {String[]} b
# @return {String[]}
def word_subsets(a, b)
  hb = Hash.new(0)
  b.each do |w|
    w.chars.group_by(&:itself).each { |k, v| hb[k] = [hb[k], v.size].max }
  end
  valid = lambda do |s|
    ss = s.chars.group_by(&:itself).to_h
    hb.each do |k, v|
      return false if !ss.key?(k) || ss[k].size < v
    end
    true
  end
  a.select { |s| valid.call(s) }
end

a = %w[amazon apple facebook google leetcode]
b = %w[l e]

p word_subsets(a, b)
