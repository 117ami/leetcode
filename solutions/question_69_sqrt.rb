# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.

# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
  min = 0
  max = x
  while min <= max
    mid = (min + max) / 2
    if mid**2 > x
      max = mid - 1
    elsif mid**2 < x
      min = mid + 1
    else
      return mid
    end
  end
  max
end

p my_sqrt(4)
