#!/usr/bin/ruby -w

# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
MAX = 2**31
def divide(dividend, divisor)
  return MAX - 1 if divisor.zero?
  sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1
  divisor = divisor.abs
  dividend = dividend.abs
  res = 0

  while dividend >= divisor
    tmp = divisor
    multiple = 1
    while dividend >= (tmp << 1)
      tmp <<= 1
      multiple <<= 1
    end
    dividend -= tmp
    res += multiple
  end

  res = sign == 1 ? [MAX - 1, res].min : 0 - [MAX, res].min
end

p divide(24, 4)
