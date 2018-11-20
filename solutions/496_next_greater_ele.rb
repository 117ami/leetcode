#  You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# @param {Integer[]} find_nums
# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_element(find_nums, nums)
  stack = []
  mmp = Hash.new(-1)
  nums.each do |n|
    mmp[stack.pop] = n while !stack.empty? && stack[-1] < n
    stack << n
  end
  find_nums.map { |n| mmp[n] }
end

arr = (1..10).to_a.shuffle
find_nums = arr.shuffle.sample(3)
p [arr, find_nums]
p next_greater_element(find_nums, arr)
