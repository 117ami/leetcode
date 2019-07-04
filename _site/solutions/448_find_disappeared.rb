# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

# @param {Integer[]} nums
# @return {Integer[]}
def find_disappeared_numbers(nums)
  return [] if nums.empty?
  j = 0
  i = nums[0]
  loop do
    if nums[i - 1] != i
      t = nums[i - 1]
      nums[i - 1] = i
      i = t
    else
      i = nums[j]
      j += 1
      break if j > nums.size
    end
    p [j, nums]
  end

  r = []
  nums.each_with_index do |n, i|
    r << i + 1 if n != i + 1
  end
  r
end

def m2(nums)
  return nums if nums.empty?
  h = Hash[(1..nums.size).zip([0])]
  nums.each { |n| h.delete(n) }
  p h.keys
end

nums = [4, 3, 2, 7, 7, 2, 3, 1]
p find_disappeared_numbers(nums)
m2(nums)
