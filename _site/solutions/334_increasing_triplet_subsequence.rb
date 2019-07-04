#
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] &lt; arr[j] &lt; arr[k] given 0 &le; i &lt; j &lt; k &le; n-1
# else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
# Given [5, 4, 3, 2, 1],
# return false.
# Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

# @param {Integer[]} nums
# @return {Boolean}
def increasing_triplet(nums)
  a = b = Float::INFINITY
  nums.each do |n|
    a = [a, n].min
    b = [b, n].min if n > a
    return true if n > b
  end
  false
end

nums = Array.new(5) { Random.rand(10) }
p nums
p increasing_triplet(nums)
