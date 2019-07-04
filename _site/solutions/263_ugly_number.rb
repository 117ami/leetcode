# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note:
#
#     1 is typically treated as an ugly number.
#     Input is within the 32-bit signed integer range.

# @param {Integer} num
# @return {Boolean}
def is_ugly(num)
  return false if num <= 0
  return true if num <= 3
  num /= 2 while num.even?
  num /= 3 while num % 3 == 0
  num /= 5 while num % 5 == 0
  num == 1
end

num = Random.rand(100_000_000_000_000_000)
num = -2147483648
p num
p is_ugly(num)
