#!/usr/bin/ruby -w

# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
  return 0 if nums.empty? || target < nums[0]
  return nums.size if target > nums[-1]
  nums.each_index.map { |i| return i if target <= nums[i] }
end

nums = [1, 2, 3, 7]
target = 1
p search_insert(nums, target)
