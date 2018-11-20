# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
# Example:
# Input: 4, 14, 2
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Note:
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4.
#

# @param {Integer[]} nums
# @return {Integer}
def total_hamming_distance(nums)
  return 0 if nums.size <= 1
  res = 0
  31.times do
    counters = [0, 0]
    nums.each_with_index do |n, i|
      counters[n & 1] += 1
      nums[i] >>= 1
    end
    res += counters[0] * counters[1]
  end
  res
end

nums = [4, 2, 14]
p total_hamming_distance(nums)
