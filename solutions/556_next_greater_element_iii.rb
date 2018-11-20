# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
# Example 1:
# Input: 12
# Output: 21
#
# Example 2:
# Input: 21
# Output: -1
#
#

def next_permutation(nums)
  return nums if nums.size <= 1
  k = Array(0..nums.size - 2).rindex { |i| nums[i] < nums[i + 1] }
  if k.nil?
    nums.sort! # The permutation, such as '54321', is the last permutation
  else
    # There must exist one, otherwise this algorithm already returned
    i = nums.rindex { |v| v > nums[k] }
    nums[k], nums[i] = nums[i], nums[k]
    nums[k + 1..-1] = nums[k + 1..-1].reverse
  end
end

# @param {Integer} n
# @return {Integer}
def next_greater_element(n)
  digits = n.to_s.chars.map(&:to_i)
  next_permutation(digits)
  m = digits.join.to_i
  m > 2**31 - 1 || m <= n ? -1 : m
end

n = 534_976
p next_greater_element(n)

