# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#

# @param {Integer[]} nums
# @return {Integer[]}
# For each number n in nums, we flip the item at location n to negative
# If n appeares for twice, then the item at location n will be flipped twice
def find_duplicates(nums)
  duplicates = []
  nums.each do |n|
    abs_n = n.abs
    if nums[abs_n - 1] < 0
      duplicates << abs_n
    else
      nums[abs_n - 1] *= -1
    end
  end
  duplicates
end

nums = [4, 3, 2, 7, 8, 2, 3, 1]
p find_duplicates(nums)
