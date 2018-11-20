
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
  return 1 if nums.empty?
  loop do
    sig = true
    nums.each_with_index do |v, i|
      next if v.nil?
      next unless v > 0 && nums[v] != v
      sig = false
      nums[i] = nums[v]
      nums[v] = v
    end
    # p nums
    break if sig
  end

  1.upto(nums.size - 1).each do |i|
    return i if i != nums[i]
  end
  nums.size
end

nums = [3, 2, 0, -1, -1, 4, 1, 7, 9, 8, 5, 6]
# nums = [1, 3, 2, 5]
# nums = [2, 2]
p first_missing_positive(nums)

