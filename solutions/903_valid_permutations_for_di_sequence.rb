# We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)
# Avalid permutationis a permutation P[0], P[1], ..., P[n] of integers{0, 1, ..., n}, such that for all i:
#   If S[i] == 'D', then P[i] > P[i+1], and;
#   If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there? Since the answer may be large, return your answer modulo 10^9 + 7.
#
# Example 1:
# Input: "DID"
# Output: 5
# Explanation:
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
# Note:
#   1 <= S.length <= 200
#   S consists only of characters from the set {'D', 'I'}.
#
#  https://leetcode.com/problems/valid-permutations-for-di-sequence/description/
require './aux.rb'

# @param {String} s
# @return {Integer}
def num_perms_di_sequence(s)
  mod = 10**9 + 7
  memo = [1]
  s.each_char.with_index do |c, idx|
    if c == 'D'
      memo << 0
      idx.downto(0).each { |j| memo[j] += memo[j + 1] }
    else
      memo.unshift(0)
      1.upto(idx + 1).each { |j| memo[j] += memo[j - 1] }
    end
    p [c, idx, memo]
  end
  memo # .reduce(:+) % mod
end

s = 'DIDDDD'
p num_perms_di_sequence(s)
