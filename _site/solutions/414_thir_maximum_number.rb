
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

# @param {Integer[]} nums
# @return {Integer}
def third_max(nums)
  return nums.max if nums.size < 3
  a = b = c = - Float::INFINITY
  nums.each do |n|
    if n > a
      c = b
      b = a
      a = n
    elsif n < a && n > b
      c = b
      b = n
    elsif n < b && n > c
      c = n
    end
  end

  r = c < - 2 << 32 ? a : c
  r
end

nums = 10.times.map { Random.rand(10) }
p nums
p third_max(nums)
