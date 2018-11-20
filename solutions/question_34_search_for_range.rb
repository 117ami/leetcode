#!/usr/bin/ruby -w

# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def left_border(nums, target)
  bdl = 0
  bdr = nums.size - 1
  left = bdr / 2

  loop do
    return -1 if nums[bdr] < target || nums[bdl] > target
    if bdr - bdl < 3
      (bdl..bdr).each { |i| return i if nums[i] == target }
      return -1
    end

    if nums[left] > target
      bdr = left
      left = (left + bdl) / 2
    elsif nums[left] < target
      bdl = left
      left = (left + bdr) / 2
    else
      return left if left.zero? || nums[left - 1] != target
      bdr = left
      left = (left + bdl) / 2
    end
  end
end

def right_border(nums, target)
  bdl = 0
  bdr = nums.size - 1
  right = bdr / 2

  loop do
    return -1 if nums[bdr] < target || nums[bdl] > target
    if bdr - bdl < 3
      Array(bdl..bdr).reverse.each { |i| return i if nums[i] == target }
      return -1
    end

    if nums[right] > target
      bdr = right
      right = (right + bdl) / 2
    elsif nums[right] < target
      bdl = right
      right = (right + bdr) / 2
    else
      return right if right == nums.size - 1 || nums[right + 1] != target
      bdl = right
      right = (right + bdr) / 2
    end
  end
end

def search_range(nums, target)
  return [-1, -1] if nums.empty?
  [left_border(nums, target), right_border(nums, target)]
end

def search_range_2(nums, target)
  left = nums.bsearch_index { |i| i > target - 1 } || -1
  left = -1 if nums[left] != target
  right = left == -1 ? -1 : (nums.bsearch_index { |i| i > target } || nums.size) - 1
  [left, right]
end

nums = [2, 3, 4, 5, 7, 7, 8, 8, 9, 10, 12]
target = 7
# nums = [2, 2, 2, 2, 3]
# target = 2
p search_range_2(nums, target)

exit
p [*nums.each_with_index].bsearch { |x, _| x > 7 }
p (0..nums.size - 1).bsearch { |i| nums[i] > 7 }
p (0..nums.size - 1).bsearch { |i| nums[i] > 8 }
