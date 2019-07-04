#
# @lc app=leetcode id=3 lang=ruby
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.12%)
# Total Accepted:    862.5K
# Total Submissions: 3.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  res = 0
  left_idx = -1
  char_to_idx= {}
  
  s.each_char.with_index do |c, i|
  	cur_idx = char_to_idx[c] || -1
  	left_idx = cur_idx if cur_idx > left_idx 
  	char_to_idx[c] = i 
  	res = [res, i - left_idx].max
  end
  res
end

s = 'bbbbb'
# s = 'tmmzuxt'
p length_of_longest_substring(s)
