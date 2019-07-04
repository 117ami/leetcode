#  Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# Example:
# nums = [1, 2, 3]
# target = 4
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
# Credits:Special thanks to @pbrother for adding this problem and creating all test cases.
#  https://leetcode.com/problems/combination-sum-iv/description/
require './aux.rb'

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def combination_sum4(nums, target)
  nums.sort!
  res = Array.new(target + 1, 0)
  1.upto(res.size - 1).each do |i|
    nums.each do |n|
      break if n > i
      res[i] += if i > n
                  res[i - n]
                else
                  1
                end
    end
  end
  res.last
end

nums = [1, 2, 3]
target = 4
p combination_sum4(nums, target)
