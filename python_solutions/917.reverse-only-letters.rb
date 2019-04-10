#
# @lc app=leetcode id=917 lang=ruby
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.98%)
# Total Accepted:    22.7K
# Total Submissions: 40.7K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
#
#
#
#
#
#
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
# Input: "ab-cd"
# Output: "dc-ba"
#
#
#
# Example 2:
#
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
#
#
# Example 3:
#
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#
# Note:
#
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
#
#
#
#
#
#
# @param {String} s
# @return {String}
def isletter?(c)
  c =~ /[[:alpha:]]/ || false
end

def reverse_only_letters(s)
  i = 0
  j = s.size - 1
  while i < j
    i += 1 while i < j && !isletter?(s[i])
    j -= 1 while i < j && !isletter?(s[j])
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
  end
  s
end

s = 'abc'
s = 'a-bC-dEf-ghIj'
s = 'Test1ng-Leet=code-Q!'
p reverse_only_letters(s)
