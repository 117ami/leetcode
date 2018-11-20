
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  left = 0
  pre = Hash.new(0)
  nums.each do |v|
    if pre[v] < 2
      nums[left] = v
      left += 1
    end
    pre[v] += 1
  end
  left
end

# METHOD 2
def remove_duplicates_2(nums)
  r = 0
  nums.each do |v|
    if r < 2 || v > nums[r - 2]
      nums[r] = v
      r += 1
    end
  end
  r
end

n = [1, 1, 1, 2, 2, 2, 2, 3, 3]
p remove_duplicates_2([1, 1, 1])
