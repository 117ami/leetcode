# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
#

# @param {Integer[]} nums
# @return {Integer}
def triangle_number(nums)
  nums.sort!
  nums.shift until nums.empty? || !nums[0].zero?
  si = nums.size
  return 0 if si < 3
  r = 0
  (0..si - 3).each do |i|
    na = nums[i]
    (i + 1..si - 2).each do |j|
      nb = nums[j]
      z = nums.bsearch_index { |v| v > na + nb - 1 }
      r += if z.nil?
             si - 1 - j
           else
             z - j - 1
           end
    end
  end
  r
end

def triangle_number_2(nums)
  nums.sort!
  c = 0
  si = nums.size
  (0..si - 1).each do |i|
    l = 0
    r = i - 1
    while l < r
      if nums[r] + nums[l] > nums[i]
        c += r - l
        r -= 1
      else
        l += 1
      end
    end
  end
  c
end

nums = [2, 2, 3, 4]
nums = 30.times.map { Random.rand(100) }
# nums = Array(2..10)
# nums = [0, 0, 0]
p nums
p triangle_number(nums)
p triangle_number_2(nums)
