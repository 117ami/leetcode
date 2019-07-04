#!/usr/bin/ruby -w

# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
  # return nums.permutation(nums.size).to_a
  case nums.size
  when 0
    nums
  when 1
    [nums]
  when 2
    [nums, nums.reverse]
  else
    r = []
    nums.each_index do |i|
      tmp = Array.new(nums)
      tmp.delete_at(i)
      permute(tmp).each do |p|
        r << [nums[i]] + p
      end
    end
    r
  end
end

nums = [1, 2, 3]
p permute(nums)
