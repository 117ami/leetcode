#
# @lc app=leetcode id=336 lang=ruby
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (31.02%)
# Total Accepted:    70.1K
# Total Submissions: 225.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in
# the given list, so that the concatenation of the two words, i.e. words[i] +
# words[j] is a palindrome.
#
# Example 1:
#
#
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
#
# Example 2:
#
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
#
#
#
#
# @param {String[]} words
# @return {Integer[][]}
def palindrome_pairs(words)
  res = []
  m = {}
  words.each_with_index do |w, i|
    m[w.reverse] = i
  end

  words.each_with_index do |w, i|
    0.upto(w.size - 1).each do |j|
      if is_palindrome?(w[j + 1..w.size - 1]) && m.key?(w[0..j])
        res << [i, m[w[0..j]]]
      end
    end

    res << [i, m['']] if is_palindrome?(w) && m.key?('')

    (w.size - 1).downto(0).each do |j|
      if is_palindrome?(w[0..j]) && m.key?(w[j + 1..w.size - 1])
        res << [m[w[j + 1..w.size - 1]], i]
      end
    end
  end
  res.reject { |a, b| a == b }
end

def is_palindrome?(str)
  return true if str.size < 2

  i = 0
  j = str.size - 1
  while i < j
    return false if str[i] != str[j]

    i += 1
    j -= 1
  end
  true
end

words = ['abcd', 'dcba', 'lls', 's', 'sssll', '']
# words = ["s", ""]
# words = ["bat","tab","cat"]
p palindrome_pairs(words)
