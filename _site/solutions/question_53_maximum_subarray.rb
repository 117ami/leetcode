# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
  return 0 if nums.empty?
  rmax = nums[0]
  tmax = nums[0]
  1.upto(nums.size - 1).each do |i|
    tmax = [tmax + nums[i], nums[i]].max
    rmax = [rmax, tmax].max
  end
  rmax
end

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
p max_sub_array(nums)
