
# Given an array S of n integers, find three integers in S such that the sum
#  is closest to a given number, target. Return the sum of the three integers.
#  You may assume that each input would have exactly one solution.

def three_sum_closest(nums, target)
  return nums.sum if nums.sort!.size <= 3
  res = nums[0..2].sum
  
  (0..nums.size - 3).each do |i|
    j = i + 1
    k = nums.size - 1
    while j < k
      sum = nums[i] + nums[j] + nums[k]
      return target if sum == target
      res = sum if (target - sum).abs < (target - res).abs
      j += 1 if sum < target
      k -= 1 if sum > target
    end
  end
  res
end

p three_sum_closest([1, 2, -1, -4, 3], 1)
