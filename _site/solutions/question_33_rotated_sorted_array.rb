
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
# Assume nums is not empty
def whereis_pivot(nums)
  ia = 0
  ib = nums.size - 1
  middle = (ia + ib) / 2
  while ia < ib
    if nums[ia] < nums[middle]
      ia = middle
    else
      ib = middle
    end
    middle = (ia + ib) / 2
  end
  ia
end

def mybsearch(nums, target)
  id = nums.bsearch_index { |v| v > target - 1 }
  res = id.nil? || nums[id] != target ? nil : id
  res
end

def search(nums, target)
  return -1 if nums.empty?
  pivot = whereis_pivot(nums)
  ia = mybsearch(nums[0..pivot], target)
  ib = mybsearch(nums[pivot + 1..nums.size - 1], target)
  ia.nil? ? (ib.nil? ? -1 : pivot + 1 + ib) : ia
end

def search_2(nums, target)
  return -1 if nums.empty?
  id = nums.index(target)
  id.nil? ? -1 : id
end

nums = [3, 1]
id = search_2(nums, 1)
p id

# arr = Array(2..9)
# p arr.each_with_index.to_a.bsearch { |(x, _id)| x == 3 }
# p arr.bsearch_first { |x| x == 3 }
