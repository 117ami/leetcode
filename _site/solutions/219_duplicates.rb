# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
  v = {}
  nums.each_with_index do |n, i|
    return true if v.key?(n) && i - v[n] <= k
    v[n] = i
  end
  false
end

nums = (1..10).map { Random.rand(10) }
p nums
p contains_nearby_duplicate(nums, 3)
