# Given an integer array of size n, find all elements that appear more than &lfloor; n/3 &rfloor; times.
# Note: The algorithm should run in linear time and in O(1) space.
# Example 1:
# Input: [3,2,3]
# Output: [3]
# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
#

# @param {Integer[]} nums
# @return {Integer[]}
def majority_element(nums)
  cache = Hash.new(0).tap { |h| nums.each { |i| h[i] += 1 } }
  sen = nums.size / 3
  cache.keys.keep_if { |k| cache[k] > sen }
end

def majority_element2(nums)
  cana = canb = ctera = cterb = 0
  nums.each do |n|
    if n == cana
      ctera += 1
    elsif n == canb
      cterb += 1
    elsif ctera.zero?
      ctera = 1
      cana = n
    elsif cterb.zero?
      cterb = 1
      canb = n
    else
      ctera -= 1
      cterb -= 1
    end
  end
  [cana, canb].keep_if { |c| nums.count(c) > nums.size / 3 }.uniq
end

nums = [1, 1, 1, 2, 2, 3, 2, 3]
nums = [3, 0, 3, 4]
nums = [0, 0, 0]
p majority_element(nums)
p majority_element2(nums)
