# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
  words = str.split
  return false unless words.size == pattern.length
  mat = {}
  val = {}
  pattern.each_char.with_index do |c, i|
    return false if mat[c].nil? && val.key?(words[i]) || !mat[c].nil? && mat[c] != words[i]
    mat[c] = words[i]
    val[words[i]] = nil
  end
  true
end

def word_pattern_2(pattern, str)
  words = str.split
  return false unless words.size == pattern.length
  pat = {}
  wor = {}
  pattern.chars.zip(words).each_with_index do |(p, w), i|
    return false unless pat[p] == wor[w]
    pat[p] = wor[w] = i
  end
  true
end

pattern = 'aaaa'
str = 'dog cat cat dog'
p word_pattern(pattern, str)
p word_pattern_2(pattern, str)
