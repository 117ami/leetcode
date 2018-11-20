# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.  If there is more than one possible answer, return the longest word with the smallest lexicographical order.  If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
#
#  https://leetcode.com/problems/longest-word-in-dictionary/description/

# @param {String[]} words
# @return {String}
def longest_word(words)
  words.sort_by!(&:size)
  p words
  res = ''
  return res if words.empty? || words[0].size != 1
  cache = Hash.new(false)
  res = words[0]
  words.each_with_index do |w, i|
    if w.size == 1
      cache[w] = true
      res = res < w ? res : w
    end

    i.downto(0).each do |j|
      next if words[j].size == w.size
      break if words[j].size < w.size - 1
      next unless words[j] + w[-1] == w && cache[words[j]]
      cache[w] = true
       res = w.size > res.size ? w : w.size == res.size ? [w, res].min : res
    end
  end
  res
end

words = %w[a banana app appl ap apply apple]
words = %w[w wo wor worl world]
words = %w[m mo moc moch mocha l la lat latt latte c ca cat]
p longest_word(words)
