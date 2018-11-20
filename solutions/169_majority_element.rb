
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
  nums.sort[nums.size / 2]
end

def majority_element2(nums)
  h = {}
  nums.each do |n|
    if h.key?(n)
      return n if h[n] + 1 > nums.size / 2.0
      h[n] += 1
    else
      h[n] = 1
    end
  end
  nums[0]
end
