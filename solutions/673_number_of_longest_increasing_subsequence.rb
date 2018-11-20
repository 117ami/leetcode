#
# Given an unsorted array of integers, find the number of longest increasing subsequence.
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note:
# Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
#
#  https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {Integer}
def find_number_of_lis(nums)
  len = Array.new(nums.size, 1)
  cnt = Array.new(nums.size, 1)
  res = max_len = 0
  0.upto(nums.size - 1).each do |i|
    0.upto(i - 1).each do |j|
      next if nums[i] <= nums[j]
      cnt[i] += cnt[j] if len[i] == len[j] + 1
      if len[i] < len[j] + 1
        len[i] = len[j] + 1
        cnt[i] = cnt[j]
      end
    end
    res += cnt[i] if max_len == len[i]
    if max_len < len[i]
      max_len = len[i]
      res = cnt[i]
    end
  end
  # p len, cnt
  res
end

nums = [1, 3, 5, 4, 7, 6]
nums = [1, 2, 4, 3, 5, 4, 7, 2]
p find_number_of_lis(nums)
