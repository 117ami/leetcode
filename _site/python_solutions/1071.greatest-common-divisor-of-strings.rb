#
# @lc app=leetcode id=1071 lang=ruby
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (48.82%)
# Total Accepted:    3.1K
# Total Submissions: 6.4K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
# concatenated with itself 1 or more times)
#
# Return the largest string X such that X divides str1 and X divides str2.
#
#
#
# Example 1:
#
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
# Example 2:
#
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
# Example 3:
#
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
#
#
# Note:
#
#
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.
#
#
# @param {String} str1
# @param {String} str2
# @return {String}
def gcd(a, b)
  b == 0 ? a : gcd(b, a.modulo(b))
end

def divide(s, m)
  0.upto(s.size - 1).each do |i|
    return false if s[i] != s[i % m]
  end
  true
end

def gcd_of_strings(s1, s2)
  m = gcd(s1.size, s2.size)
  return s1[0..m - 1] if divide(s1, m) && divide(s2, m) && s1[0..m - 1] == s2[0..m - 1]

  ''
end

str1 = 'ABABAB'
str2 = 'AB'
p gcd_of_strings(str1, str2)
