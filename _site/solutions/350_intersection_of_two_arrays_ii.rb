#
# Given two arrays, write a function to compute their intersection.
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  nums2.sort!
  nums1.sort!
  ans = []
  i = j = 0
  while i < nums1.size && j < nums2.size
    if nums1[i] == nums2[j]
      ans << nums2[j]
      i += 1
      j += 1
    elsif nums1[i] < nums2[j]
      i += 1
    else
      j += 1
    end
  end
  ans
end

nums1 = [1, 2, 3, 2]
nums2 = [2, 3]
p intersect(nums1, nums2)
