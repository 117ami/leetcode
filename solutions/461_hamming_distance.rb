# coding: utf-8
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def hamming_distance(x, y)
  return 0 if x == y
  x, y = y, x if x > y
  s1 = x.to_s(2)
  s2 = y.to_s(2)
  r = 0
  i = 1
  while i <= s1.size
    r += 1 if s1[-i] != s2[-i]
    i += 1
  end

  (i..s2.size).each { |j| r += 1 if s2[-j] == '1' }
  r
end

def hamming_distance2(x, y)
  (x ^ y).to_s(2).count('1')
end

x = Random.rand(100)
y = Random.rand(100)
p [x, y]
p hamming_distance(x, y)
p hamming_distance2(x, y)

p 2 ^ 2
