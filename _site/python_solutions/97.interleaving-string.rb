#
# @lc app=leetcode id=97 lang=ruby
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.01%)
# Total Accepted:    111.8K
# Total Submissions: 398.7K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#
# @param {String} s1
# @param {String} s2
# @param {String} s3
# @return {Boolean}
# determinate is s.chars is a sublist of t.chars. e.g., is_sub?('abc', 'apbpcp') == True
def is_sub?(s, t)
  i = j = 0
  while i < s.size && j < t.size
    i += 1 if s[i] == t[j]
    j += 1
  end
  i == s.size
end

def array_array(rn, cn, iv = 1)
  Array.new(rn) { Array.new(cn, iv) }
end

def is_interleave(s1, s2, s3)
  return false unless s1.size + s2.size == s3.size
  return false unless is_sub?(s1, s3) && is_sub?(s2, s3)

  dp = array_array(s1.size + 1, s2.size + 1, false)
  0.upto(s1.size).each do |i|
    0.upto(s2.size).each do |j|
      if i.zero? && j.zero?
        dp[i][j] = true
      elsif i.zero?
        dp[i][j] = dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]
      elsif j.zero?
        dp[i][j] = dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]
      else
        dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
      end
    end
  end
  dp.last.last
end

s1 = 'aabcc'
s2 = 'dbbca'
s3 = 'aadbbcbcac'
p is_interleave(s1, s2, s3)
