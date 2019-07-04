# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# @param {Integer[]} nums
# @return {Integer}
def rob(nums)                   # leetcode 36ms
  return 0 if nums.empty?
  return nums.max if nums.size < 3
  pre = [0, 'n']
  res = [nums[0], 'y']
  nums[1..-2].each do |n|
    tmp = [pre[0], pre[1]]
    pre = [res[0], res[1]]
    res = [tmp[0] + n, tmp[1]] if res[0] < tmp[0] + n
  end

  return res[0] if res[0] >= nums[-1] + pre[0] # will never rob the last house
  return nums[-1] + pre[0] if pre[1] == 'n'
  cand = res[0]
  tmp = 0
  res = nums[1]
  nums[2..-1].each do |n|
    tmp, res = res, [res, n + tmp].max
  end
  [cand, res].max
end


def rob2(nums)                  # leetcode 40ms
  return 0 if nums.empty?
  return nums.max if nums.size < 3
  aux = -> (a) do
    t, r = 0, a[0]
    a[1..-1].each { |v| t, r = r, [r, t + v].max }
    r
  end
  # The first and last houses will always have a lucky one
  [aux.call(nums[0..-2]), aux.call(nums[1..-1])].max
end

nums = Array.new(2000000) { Random.rand(100) }
#p rob(nums)
p rob2(nums)
