#
# @lc app=leetcode id=884 lang=ruby
#
# [884] Uncommon Words from Two Sentences
#
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (60.41%)
# Total Accepted:    20.7K
# Total Submissions: 34.2K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# We are given two sentences A and B.  (A sentence is a string of space
# separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences, and
# does not appear in the other sentence.
#
# Return a list of all uncommon words. 
#
# You may return the list in any order.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
#
#
#
# Example 2:
#
#
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
#
#
#
#
# Note:
#
#
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.
#
#
#
#
#
# @param {String} a
# @param {String} b
# @return {String[]}
def uncommon_from_sentences(a, b)
  counter = Hash.new(0)
  a.split(' ').each do |w|
    counter[w] += 1
  end

  b.split(' ').each do |w|
    counter[w] += 1
  end
  counter.select { |_, v| v == 1 }.map(&:first)
end

a = 'this is apple is sweet'
b = 'this apple is sour'
p uncommon_from_sentences(a, b)
