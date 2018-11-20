
# Given a 32-bit signed integer, reverse digits of an integer.
# @param {Integer} x
# @return {Integer}
def reverse(x)
  return 0 if x.zero?
  flag = x < 0 ? -1 : 1

  a = x.abs.to_s.split('').reverse!.drop_while { |i| i.to_i < 1 }
  res = a.join('').to_i

  return 0 if res > 2**31 - 1
  flag * res
end
