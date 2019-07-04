#
#  Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
# Note: Your solution should run in O(log n) time and O(1) space.
#

# @param {Integer[]} nums
# @return {Integer}
def single_non_duplicate(nums)
  nums[(0..nums.size - 1).bsearch { |i| nums[i] != nums[i ^ 1] }]
end

nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 8, 8]
# nums = [3,3,7,7,10,11,11]
p single_non_duplicate(nums)
p single_non_duplicate2(nums)
(0..10).each do |i|
  p [i, i ^ 1]
end
