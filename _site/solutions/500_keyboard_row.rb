# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#
#  https://leetcode.com/problems/keyboard-row/description/
require './aux.rb'

# @param {String[]} words
# @return {String[]}
def find_words(words)
  rows = {}
  %w[qwertyuiop asdfghjkl zxcvbnm].each_with_index { |s, idx| s.each_char { |c| rows[c] = idx } }
  words.select { |w| w.chars.map { |c| rows[c.downcase] }.uniq.size == 1 }
end

words = %w[Hello Alaska Dad Peace]
p find_words(words)
