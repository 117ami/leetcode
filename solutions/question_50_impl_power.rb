
# Implement pow(x, n).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100

# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
  sign = n < 0
  n = n.abs
  res = 1

  while n > 1
    multiple = 1
    tmpres = x
    while multiple << 1 < n
      tmpres *= tmpres
      multiple <<= 1
    end
    n -= multiple
    res *= tmpres
  end

  Array.new(n) { res *= x }
  res = 1.0 / res if sign
  res
end

x = 0.00001
n = 2_147_483_647

x = 34
n = 3

p my_pow(x, n)
