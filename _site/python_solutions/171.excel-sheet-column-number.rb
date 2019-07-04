#
# @lc app=leetcode id=171 lang=ruby
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (50.35%)
# Total Accepted:    198.9K
# Total Submissions: 394.9K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#
# @param {String} s
# @return {Integer}
def title_to_number(s)
  res = 0
  s.each_char { |c| res = res * 26 + (c.ord + 1 - 'A'.ord) }
  res
end

p title_to_number('ZY')
