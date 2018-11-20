# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
  h = {}
  numbers.each_with_index do |n, i|
    return [h[target - n], i + 1] if h.key?(target - n)
    h[n] = i + 1
  end
end

numbers = 10.times.map { Random.rand(10) }
p numbers
p two_sum(numbers, 8)
