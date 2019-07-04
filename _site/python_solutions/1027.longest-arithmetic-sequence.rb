#
# @lc app=leetcode id=1027 lang=ruby
#
# [1027] Longest Arithmetic Sequence
#
# https://leetcode.com/problems/longest-arithmetic-sequence/description/
#
# algorithms
# Medium (43.04%)
# Total Accepted:    4.2K
# Total Submissions: 9.6K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array A of integers, return the length of the longest arithmetic
# subsequence in A.
#
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0
# <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
# if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
#
#
#
# Example 1:
#
#
# Input: [3,6,9,12]
# Output: 4
# Explanation:
# The whole array is an arithmetic sequence with steps of length = 3.
#
#
#
# Example 2:
#
#
# Input: [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].
#
#
#
# Example 3:
#
#
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].
#
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
#
#
#
# @param {Integer[]} a
# @return {Integer}
def longest_arith_seq_length(a)
  dp = {}
  res = 2
  0.upto(a.size - 1).each do |i|
    (i + 1).upto(a.size - 1).each do |j|
      d = a[j] - a[i]
      if dp.key?(d)
        dp[d][j] = if dp[d].key?(i)
                     dp[d][i] + 1
                   else
                     2
                   end
      else
        dp[d] = { j => 2 }
      end
      res = [res, dp[d][j]].max
    end
  end
  res
end

a = [20, 1, 15, 3, 10, 5, 8]
p longest_arith_seq_length(a)



