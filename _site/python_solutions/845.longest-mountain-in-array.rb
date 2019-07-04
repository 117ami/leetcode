#
# @lc app=leetcode id=845 lang=ruby
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (33.13%)
# Total Accepted:    13.3K
# Total Submissions: 39.5K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following
# properties hold:
#
#
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
# B[i] > B[i+1] > ... > B[B.length - 1]
#
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain. 
#
# Return 0 if there is no mountain.
#
# Example 1:
#
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
#
# Note:
#
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
#
#
# Follow up:
#
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
#
#
#
# @param {Integer[]} a
# @return {Integer}
def longest_mountain(a)
  ans = up = down = 0
  1.upto(a.size - 1).each do |i|
    up = down = 0 if down > 0 && a[i - 1] < a[i] || a[i - 1] == a[i]
    up += a[i - 1] < a[i] ? 1 : 0
    down += a[i - 1] > a[i] ? 1 : 0
    ans = [ans, up + down + 1].max if up > 0 && down > 0
  end
  ans > 2 ? ans : 0
end

a = [2, 1, 4, 7, 3, 2, 5]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p longest_mountain(a)
