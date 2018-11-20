# Given string S and adictionary of words words, find the number of words[i] that is a subsequence of S.
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# Note:
#   All words in words and S will only consists of lowercase letters.
#   The length of S will be in the range of [1, 50000].
#   The length of words will be in the range of[1, 5000].
#   The length of words[i] will be in the range of [1, 50].
#
#  https://leetcode.com/problems/number-of-matching-subsequences/description/
require './aux.rb'
# @param {String} s
# @param {String[]} words
# @return {Integer}
def subseq?(sa, map)
  seen = Hash.new(0)
  prev_idx = -1
  sa.each_char do |c|
    return false unless map.key?(c)
    return false if seen.key?(c) && map[c][seen[c]].nil?
    i = seen[c]
    i += 1 while i < map[c].size && map[c][i] < prev_idx
    return false if i == map[c].size
    prev_idx = map[c][i]
    seen[c] = i + 1
  end
  true
end

def num_matching_subseq(s, words)
  map = Hash.new { |h, k| h[k] = [] }
  s.each_char.with_index { |c, idx| map[c] << idx }
  words.count { |w| subseq?(w, map) }
end

def method2(s, words)
  pending = Hash.new { |h, k| h[k] = [] }
  words.each {|w| pending[w[0]] << [w, 1] }
  s.each_char do |c|
  	pending.delete(c) &.each {|w, i| pending[w[i]] << [w, i+1]}
  end
  pending[nil].size
end

s = 'addbcdeadc'
words = %w[a bb acd ace]

p num_matching_subseq(s, words)
p method2(s, words)
