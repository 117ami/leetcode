#
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
#
#  https://leetcode.com/problems/delete-operation-for-two-strings/description/
require './aux.rb'

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
  dp = Array.new(word1.size + 1) { Array.new(word2.size + 1, 0) }
  0.upto(word1.size).each { |i| dp[i][0] = i }

  0.upto(word2.size).each { |j| dp[0][j] = j }

  0.upto(word1.size - 1).each do |i|
    0.upto(word2.size - 1).each do |j|
      dp[i + 1][j + 1] = if word1[i] == word2[j]
                           dp[i][j]
                         else
                           [dp[i][j + 1], dp[i + 1][j]].min + 1
                 end
    end
  end
  dp.last.last
end

word1 = 'seap'
word2 = 'eatp'
p min_distance(word1, word2)
