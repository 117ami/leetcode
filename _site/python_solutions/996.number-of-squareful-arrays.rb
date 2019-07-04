#
# @lc app=leetcode id=996 lang=ruby
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (47.67%)
# Total Accepted:    4.3K
# Total Submissions: 8.9K
# Testcase Example:  '[1,17,8]'
#
# Given an array A of non-negative integers, the array is squareful if for
# every pair of adjacent elements, their sum is a perfect square.
#
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] !=
# A2[i].
#
#
#
# Example 1:
#
#
# Input: [1,17,8]
# Output: 2
# Explanation:
# [1,8,17] and [17,8,1] are the valid permutations.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 1
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
#
#
# @param {Integer[]} a
# @return {Integer}
def num_squareful_perms(a)
  return 0 if a.size == 1

  ans = 0
  prefixes = {}
  dfs = lambda do |pf, n, arr|
    ans += 1 if arr.empty?
    p [pf, n, arr, ans]
    return if arr.empty? || prefixes.key?(pf)

    arr.each_with_index do |k, i|
      next if i < arr.size - 1 && arr[i] == arr[i+1]

      z = k + n < 0 ? 3.14: Math.sqrt(k + n)
      next unless z.to_i == z || n == -1

      left = i.zero? ? [] : arr[0..i - 1]
      right = i == arr.size - 1 ? [] : arr[i + 1..-1]

      nextpf = [pf, k.to_s].join('/')
      dfs.call(nextpf, arr[i], left + right)
      prefixes[nextpf] = nil
    end
  end
  dfs.call('', -1, a)
  p prefixes
  ans
end

a = [1, 8, 8, 17]
a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 14]
a = [2, 2, 14]
# a = [0,0,0,1,1,1]
p num_squareful_perms(a)
# p Math.sqrt(0) == 0
