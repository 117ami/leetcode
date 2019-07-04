
# Given an array S of n integers, are there elements a, b, c, and d in S such
#  that a + b + c + d = target? Find all unique quadruplets in the array which
#  gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def say(*args)
  print args, "\n"
end

def bound_test(nums, target)
  # the size of nums is assumed to be below 4 here
  return [[]] if nums.size < 4 || nums.size == 4 && nums.sum != target
  [nums]
end

def four_sum(nums, target)
  return bound_test(nums, target) if nums.size <= 4
  sz = nums.sort!.size
  res = {}
  (0..sz - 4).each do |i|
    (i + 3..sz - 1).reverse_each do |j|
      say i, j, nums[i], nums[j]
      k = i + 1
      m = j - 1
      while k < m
        sum = [nums[i], nums[j], nums[k], nums[m]].sum
        if sum == target
          res[[nums[i], nums[k], nums[m], nums[j]]] = nil
          k += 1
          m -= 1
        end
        k += 1 if sum < target
        m -= 1 if sum > target
      end
    end
  end
  res.keys
end

s = [1, 0, -1, 0, 2, -2]
target = 0
p four_sum(s, target)
