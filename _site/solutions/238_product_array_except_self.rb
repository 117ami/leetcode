
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
  zn = 0
  pro = 1
  zloc = 0
  nums.each_with_index do |n, i|
    if n.zero?
      zn += 1
      zloc = i
    else
      pro *= n
    end
  end

  return [0] * nums.size if zn >= 2
  return (0..nums.size - 1).map { |j| j == zloc ? pro : 0 } if zn == 1
  (0..nums.size - 1).map { |j| (pro * nums[j]**-1).to_i }
end

def product_except_self2(nums)
  r = [1] * nums.size
  pi = 1
  pj = 1
  (0..nums.size - 1).each do |i|
    r[i] *= pi
    r[-i - 1] *= pj
    pi *= nums[i]
    pj *= nums[-i - 1]
  end
  r
end

nums = Array(2..5)
nums = [2, 3, 5, 6, 0]
# nums << 7
p product_except_self2(nums)
