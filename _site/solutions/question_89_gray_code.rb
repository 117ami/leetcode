
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

# @param {Integer} n
# @return {Integer[]}
def gray_code(n)
  return [0] if n.zero?
  r = [0, 1]
  i = 1
  while i < n
    r.dup.reverse_each { |v| r << v + 2**i }
    i += 1
  end
  r
end

p gray_code(3)
