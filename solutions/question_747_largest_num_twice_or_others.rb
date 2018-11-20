
=begin
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
=end
# @param {Integer[]} nums
# @return {Integer}
def dominant_index(nums)
  return 0 if nums.size == 1
  max = sndmax = r = -1
  (0..nums.size-1).each do |i|
    if nums[i] > max
      max, sndmax, r = nums[i], max, i
    else
      sndmax = [sndmax, nums[i]].max
    end
  end
  r = -1 unless max >= sndmax *2
  r
end

def dominant_index_2(nums)
  return 0 if nums.size == 1
  cache = Hash[nums.zip(0..nums.size-1)].sort.to_h
  snd, max = cache.keys[-2..-1]
  return -1 if snd * 2 > max
  cache[max]
end


p dominant_index_2([1, 0, 0, 0, 3, 2, 7, 3])
