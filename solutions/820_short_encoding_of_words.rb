# Given a list of words, we may encode it by writing a reference string S and a list of indexes A.
# For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#"and indexes = [0, 2, 5].
# Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.
# What is the length of the shortest reference string S possible that encodes the given words?
# Example:
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
# Note:
#   1 <= words.length<= 2000.
#   1 <=words[i].length<= 7.
#   Each wordhas onlylowercase letters.
#
#  https://leetcode.com/problems/short-encoding-of-words/description/
require './aux.rb'

# @param {String[]} words
# @return {Integer}
def minimum_length_encoding(words)
  words.sort_by!(&:length).reverse!
  repeated = {}
  res = 0
  words.each do |w|
    next if repeated.key?(w)
    0.upto(w.length - 1).each { |j| repeated[w[j..-1]] = nil }
    res += w.length + 1
  end
  res
end

words = %w[me time you me e ou bell]
p minimum_length_encoding(words)
