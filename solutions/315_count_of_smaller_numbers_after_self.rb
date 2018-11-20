# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# Example:
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#  https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

# @param {Integer[]} nums
# @return {Integer[]}
def count_smaller(nums)
  return nums if nums.empty?
  res = [0]
  sorted = [nums.pop]
  nums.reverse_each do |n|
    idx = (0..sorted.size - 1).bsearch { |i| n <= sorted[i] } || sorted.size
    sorted.insert(idx, n)
    res.unshift(idx)
  end
  res
end
nums = [2, 2, 0, 1]

p count_smaller(nums)

arr = [10, 2, 6, 9, 4, 8, 5, 3, 7, 1]
p arr
p count_smaller(arr)

arr.insert(1, 13)
p arr
