# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
# Example 1:
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#  https://leetcode.com/problems/maximum-product-of-word-lengths/description/
require './aux.rb'

# @param {String[]} words
# @return {Integer}
def max_product(words)
  masks = Array.new(words.size, 0)
  words.sort_by!(&:length).reverse!

  words.each_with_index do |w, idx|
    w.each_char { |c| masks[idx] |= 1 << (c.ord - 97) }
  end
  maxlen = 0
  0.upto(words.size - 1).each do |i|
    return maxlen if words[i].length * words[i].length <= maxlen
    (i + 1).upto(words.size - 1).each do |j|
      if masks[i] & masks[j] == 0
        maxlen = [maxlen, words[i].length * words[j].length].max
        break
      end
    end
  end
  maxlen
end

words = %w[abcw baz foo bar xtfn abcdef]
words = %w[a ab abc d cd bcd abcd]
p max_product(words)
