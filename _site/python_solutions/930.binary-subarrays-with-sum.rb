#
# @lc app=leetcode id=930 lang=ruby
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (37.53%)
# Total Accepted:    8.8K
# Total Submissions: 23.4K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#
#
# Example 1:
#
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
#
#
# Note:
#
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
#
#
# @param {Integer[]} a
# @param {Integer} s
# @return {Integer}
def num_subarrays_with_sum(a, s)
  c = Hash.new(0)
  c[0] = 1
  res = psum = 0
  a.each do |n|
    psum += n
    res += c[psum - s]
    c[psum] += 1
    p [n, c]
  end
  p c
  res
end

a = [0, 0, 1, 1, 0, 1]
# a = [1, 0, 1, 0, 0, 0, 0]
# a = [1, 1]
s = 2
p num_subarrays_with_sum(a, s)
