# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} t
# @return {Boolean}
def simple_duplicate(nums, k)
  v = {}
  nums.each_with_index do |n, i|
    return true if v.key?(n) && i - v[n] <= k
    v[n] = i
  end
  false
end

def contains_nearby_almost_duplicate(nums, k, t)
  return simple_duplicate(nums, k) if t.zero?
  ranges = []
  nums.each do |n|
    ranges.shift if ranges.size == k + 1
    cur_range = [n - t, n + t]
    ranges.each { |r| return true if overlap?(r, [n, n]) }
    ranges << cur_range
  end
  false
end

# both number in epsa, epsb are sorted
def overlap?(epsa, epsb)
  return false if epsa[1] < epsb[0] || epsa[0] > epsb[1]
  true
end

nums = (1..10).map { Random.rand(20) }
p nums
p contains_nearby_almost_duplicate(nums, 2, 0)
