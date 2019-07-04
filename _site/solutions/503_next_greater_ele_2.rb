#  Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
#
# Note: The length of given array won't exceed 10000.

# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_elements(nums)
  stack = []
  mmp = Hash.new(-1)
  (0..nums.size * 2 - 1).each do |i|
    n = nums[i % nums.size]
    while !stack.empty? && nums[stack[-1]] < n
      j = stack.pop
      mmp[j] = n
    end
    stack << i % nums.size
  end
  p mmp
  # p stack
  (0..nums.size - 1).map { |i| mmp[i] }
end

arr = (1..10).to_a.shuffle
arr = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
p arr
p next_greater_elements(arr)
