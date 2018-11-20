# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#   There may be more than one LIS combination, it is only necessary for you to return the length.
#   Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
#
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
  seen = Hash.new(1)
  rmax = 0
  increase = lambda do |n|
    seen[n] = 1 if seen.empty?
    seen.keys.each do |k|
      seen[n] = k > n ? [seen[n], seen[k] + 1].max : seen[n]
    end
  end

  nums.reverse_each do |n|
    increase.call(n)
    rmax = [rmax, seen[n]].max
  end
  p seen
  rmax
end

def length_of_lis2(nums)
  lis = []
  nums.each do |n|
    i = (0...lis.length).bsearch { |j| lis[j] >= n } || lis.length
    lis[i] = n
  end
  lis.length
end

nums = [10, 9, 2, 5, 3, 7, 2, 101, 18]
# nums = [2, 2]
nums = [4, 10, 4, 3, 8, 9]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
nums = [1, 3, 6, 7, 4, 10, 5]
p length_of_lis(nums)
p length_of_lis2(nums)
