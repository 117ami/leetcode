# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
# Input: [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Example 2:
# Input: [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]

# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
  return [] if nums.empty?
  ret = []
  lt = 0
  (1..nums.size - 1).each do |i|
    next if nums[i] - nums[i - 1] == 1
    ret << if lt == i - 1
             nums[lt].to_s
           else
             [nums[lt], nums[i - 1]].join('->')
           end
    lt = i
  end
  ret << if lt == nums.size - 1
           nums[-1].to_s
         else
           [nums[lt], nums[-1]].join('->')
         end
  ret
end

nums = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
nums = [0]
p summary_ranges(nums)
