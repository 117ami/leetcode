# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
# Example:
# Input:"aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#  https://leetcode.com/problems/palindrome-partitioning-ii/description/
require './aux.rb'

# @param {String} s
# @return {Integer}
def min_cut(s)
  cut = 0.upto(s.size).to_a.map { |k| k - 1 }
  0.upto(s.size - 1).each do |i|
    0.upto(s.size - i - 1).each do |j|
      break if j > i || s[i - j] != s[i + j]
      cut[i + j + 1] = [cut[i + j + 1], 1 + cut[i - j]].min
    end

    0.upto(s.size - i - 1).each do |j|
      break if j > i + 1 || s[i - j + 1] != s[i + j]
      cut[i + j + 1] = [cut[i + j + 1], 1 + cut[i - j + 1]].min
    end
  end
  cut[s.size]
end

s = 'kaabcbaad'
p min_cut(s)
