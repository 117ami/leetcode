# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.
#

# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
  last_seen = nums.size - 1
  last_seen.downto(0) do |i|
    last_seen = i if nums[i] != 0 && i + nums[i] >= last_seen
  end
  last_seen == 0
end

n = [1, 2, 0, 1]

r = can_jump(n)
p r
