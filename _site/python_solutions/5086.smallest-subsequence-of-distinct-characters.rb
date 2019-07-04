#
# @lc app=leetcode id=5086 lang=ruby
#
# [5086] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (33.27%)
# Total Accepted:    1.4K
# Total Submissions: 3.8K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
#
#
#
# Example 1:
#
#
# Input: "cdadabcc"
# Output: "adbc"
#
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "abcd"
#
#
#
# Example 3:
#
#
# Input: "ecbacba"
# Output: "eacb"
#
#
#
# Example 4:
#
#
# Input: "leetcode"
# Output: "letcod"
#
#
#
#
# Note:
#
#
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
#
#
#
#
#
#
#
#
# @param {String} text
# @return {String}
def counter(t)
  cter = Hash.new(0)
  arr = t.is_a?(String) ? t.chars : t
  arr.each do |c|
    cter[c] += 1
  end
  cter
end

def smallest_subsequence(text)
  used = Hash.new(0)
  cnt = counter(text)
  res = []
  text.each_char do |c|
    cnt[c] -= 1
    next if used[c] > 0

    used[c] += 1
    used[res.pop] = 0 while !res.empty? && res.last > c && cnt[res.last] > 0
    res << c
  end
  res.join
end

text = 'cdadabcc'
# text = 'ddeeeccdce'
p smallest_subsequence(text)
