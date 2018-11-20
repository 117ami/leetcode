#
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
# Example1:
# a = 2
# b = [3]
# Result: 8
# Example2:
# a = 2
# b = [1,0]
# Result: 1024
# Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.

# @param {Integer} a
# @param {Integer[]} b
# @return {Integer}
@base = 1337

def super_pow(a, b)
  return 1 if b.empty?
  n = b[-1]
  b.pop
  powmod(a, n) * powmod(super_pow(a, b), 10) % @base
end

def powmod(a, k)
  a %= @base
  res = 1
  k.times { res = (res * a) % @base }
  res
end

a = 2
b = [1, 0]
p super_pow(a, b)
