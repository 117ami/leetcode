#
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input:
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
#

# @param {String} s
# @return {Integer}
def longest_palindrome_subseq(s)
  cache = Array.new(s.size) { Array.new(s.size) }
  dp(s, 0, s.size - 1, cache)
  # p cache
  cache[0][s.size - 1]
end

def dp(s, i, j, cache)
  return cache[i][j] if cache[i][j]
  return 0 if i > j
  return 1 if i == j
  cache[i][j] = if s[i] == s[j]
                  2 + dp(s, i + 1, j - 1, cache)
                else
                  [dp(s, i, j - 1, cache), dp(s, i + 1, j, cache)].max
                end
  cache[i][j]
end

s = 1000.times.map { Array('a'..'z').sample(1)[0] }.shuffle.join
p s
p longest_palindrome_subseq(s)
