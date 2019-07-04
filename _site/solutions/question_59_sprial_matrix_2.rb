#!/usr/bin/ruby -w

=begin
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
=end

def rotate(nums)
  nums.transpose.map { |v| v.reverse }
end

def generate_matrix(n)
  return [] if n.zero?
  return [[1]] if n == 1
  n = n ** 2
  r = [[n]]
  loop do
    len = r[0].size
    r.unshift(Array(n - len .. n - 1))
    n -= len
    return r if n <= 1
    r = rotate(r)
  end
end

p generate_matrix(1)
