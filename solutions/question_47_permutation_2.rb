
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

# @param {Integer[]} nums
# @return {Integer[][]}
def permute_unique(nums)
  case nums.size
  when 0
    nums
  when 1
    [nums]
  when 2
    [nums, nums.reverse].uniq
  else
    r = []
    seen = {}
    nums.each_index do |i|
      next if seen.key?(nums[i])
      seen[nums[i]] = nil
      tmp = Array.new(nums)
      tmp.delete_at(i)
      permute_unique(tmp).each do |p|
        np = [nums[i]] + p
        r << np
      end
    end
    r
  end
end

n = [1, 2, 1, 2]
p permute_unique(n)
