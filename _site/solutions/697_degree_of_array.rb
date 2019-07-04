# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

# @param {Integer[]} nums
# @return {Integer}
def find_shortest_sub_array(nums)
  res = Float::INFINITY
  frequency = Hash.new(0)
  lpos = {}
  rpos = {}
  max_freq = 0

  nums.each_with_index do |n, i|
    frequency[n] += 1
    lpos[n] = i unless lpos.key?(n)
    rpos[n] = i
    if frequency[n] == max_freq
      res = [res, rpos[n] - lpos[n]].min
    elsif frequency[n] > max_freq
      max_freq = frequency[n]
      res = rpos[n] - lpos[n]
    end
  end
  res + 1
end

def method2(nums)
  nums.each_with_index.group_by(&:first).values.map { |v| [-v.size, v[-1][1] - v[0][1] + 1] }.min[1]
end

nums = [1, 2, 2, 1, 1, 3, 4, 2]
nums = 10.times.map { Random.rand(10) }
p nums
p find_shortest_sub_array(nums)
p method2(nums)
