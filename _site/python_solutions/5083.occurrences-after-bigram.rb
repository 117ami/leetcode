#
# @lc app=leetcode id=5083 lang=ruby
#
# [5083] Occurrences After Bigram
#
# https://leetcode.com/problems/occurrences-after-bigram/description/
#
# algorithms
# Easy (70.04%)
# Total Accepted:    3.1K
# Total Submissions: 4.4K
# Testcase Example:  '"alice is a good girl she is a good student"\n"a"\n"good"'
#
# Given words first and second, consider occurrences in some text of the form
# "first second third", where second comes immediately after first, and third
# comes immediately after second.
#
# For each such occurrence, add "third" to the answer, and return the
# answer.
#
#
#
# Example 1:
#
#
# Input: text = "alice is a good girl she is a good student", first = "a",
# second = "good"
# Output: ["girl","student"]
#
#
#
# Example 2:
#
#
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]
#
#
#
#
# Note:
#
#
# 1 <= text.length <= 1000
# text consists of space separated words, where each word consists of lowercase
# English letters.
# 1 <= first.length, second.length <= 10
# first and second consist of lowercase English letters.
#
#
#
#
# @param {String} text
# @param {String} first
# @param {String} second
# @return {String[]}
def find_ocurrences(text, first, second)
  a = text.split
  res = []
  0.upto(a.size - 3).each do |i|
    next unless a[i] == first && a[i + 1] == second

    res << a[i + 2]
  end
  res
end

text = 'we will we will rock you'
first = 'we'
second = 'will'
p find_ocurrences(text, first, second)
