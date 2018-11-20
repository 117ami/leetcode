
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# Note:
# You can assume that you can always reach the last index.

# @param {Integer[]} nums
# @return {Integer}
def jump(nums)
  return 0 if nums.size <= 1
  sz = nums.size
  step = 0
  seen = Hash.new { |h, k| h[k] = [] }
  seen[0] = [0]
  bound = 0
  loop do
    seen[step].each do |i|
      next unless i + nums[i] > bound
      return step + 1 if i + nums[i] >= sz - 1
      seen[step + 1] += Array(bound + 1..i + nums[i])
      bound = i + nums[i]
    end
    step += 1
  end
end

nums = [2, 4, 2, 1, 2, 5, 1, 4]
p jump(nums)
