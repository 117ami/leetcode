# A positive integeris magicalif it is divisible by either Aor B.
# Return the N-th magical number. Since the answer may be very large, return it modulo 10^9 + 7.
#
# Example 1:
# Input: N = 1, A = 2, B = 3
# Output: 2
# Example 2:
# Input: N = 4, A = 2, B = 3
# Output: 6
# Example 3:
# Input: N = 5, A = 2, B = 4
# Output: 10
# Example 4:
# Input: N = 3, A = 6, B = 4
# Output: 8
#
# Note:
#   1 <= N<= 10^9
#   2 <= A<= 40000
#   2 <= B<= 40000
#
#  https://leetcode.com/problems/nth-magical-number/description/

# @param {Integer} n
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def nth_magical_number(n, a, b)
  a, b = [a, b].sort
  return a * n % 1_000_000_007 if a * n <= b || b % a == 0
  xlcm = a.lcm(b)
  m = n
  f = 0
  res = 0
  loop do
    y = ((a * n - a) * 1.0 / (a + b)).ceil
    x = n - y
    res = [[a * x, b * y].max, a * x + a, b * y + b].min
    n = m + res / xlcm
    p [a, b, x, y, res, n, xlcm, a * x, b * y]
    break if n - m <= f
    f = n - m
  end
  res % 1_000_000_007
end

n = 859
a = 759
b = 30
p nth_magical_number(n, a, b)
