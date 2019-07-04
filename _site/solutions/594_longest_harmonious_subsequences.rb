# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.

# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
  cache = Hash.new(0).tap { |h| nums.each { |i| h[i] += 1 } }
  maxr = 0
  cache.keys.sort.each do |k|
    next unless cache.key?(k + 1)
    maxr = [maxr, cache[k] + cache[k + 1]].max
  end
  maxr
end

nums = [1, 3, 2, 2, 5, 2, 3, 7]
# nums = [1, 1, 1, 1]
p find_lhs(nums)
