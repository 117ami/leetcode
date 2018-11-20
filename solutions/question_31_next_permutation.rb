#!/user/bin/ruby -w
# coding: utf-8
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# Lexicographically next greater permutation means: the array represents a
#  number, the job is to arrange the array to get a slightly bigger number

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def next_permutation(nums)
  return nums if nums.size <= 1
  k = Array(0..nums.size - 2).rindex { |i| nums[i] < nums[i + 1] }
  if k.nil?
    nums.sort! # The permutation is the last permutation
  else
    # There must exist one, otherwise this algorithm already returned
    i = nums.rindex { |v| v > nums[k] }
    nums[k], nums[i] = nums[i], nums[k]
    nums[k + 1..-1] = nums[k + 1..-1].reverse
  end
end

nums = [3, 2, 1]
p next_permutation(nums)

nums = [1, 2, 6, 5, 4, 3, 1]
next_permutation(nums)
k = nums.rindex { |v| v > 2 }
p k

nums = [5, 4, 3, 2, 1]
m = Array(0..nums.size - 2).rindex { |i| nums[i] < nums[i + 1] }
p m
