# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.
#
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum(nums, k)
  return true if two_serial_zeros?(nums)
  return false if k.zero?

  sums = { 0 => -1 }
  t = 0
  nums.each_with_index do |n, i|
    next if n.zero?
    t += n
    rem = t % k
    return true if sums.key?(rem) && i - sums[rem] > 1
    sums[rem] = i unless sums.key?(rem)
  end

  false
end

def two_serial_zeros?(nums)
  j = -99
  nums.each_with_index do |n, i|
    next unless n.zero?
    return true if i - j == 1
    j = i
  end
  false
end

nums = [23, 2, 4, 6, 7]
nums = 10.times.map { Random.rand(10) }
nums = [0, 0, 0, 3, 2, 1, 7, 9]
p nums
p check_subarray_sum(nums, 3)
