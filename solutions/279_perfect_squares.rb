# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#  https://leetcode.com/problems/perfect-squares/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
# if you are familiar with Legendre's three square theorem,
# you can solve this problem with a better solution.
def perfect_number?(n)
  return true if n.zero?
  k = Math.sqrt(n).to_i
  k * k == n
end

def num_squares(n)
  return 1 if perfect_number?(n)
  # By Legendre's law, the result if 4 if n = 4^a(8b + 7)
  n >>= 2 while n & 3 == 0
  return 4 if n & 7 == 7

  sqrtn = Math.sqrt(n).to_i
  1.upto(sqrtn).each do |k|
    break if k * k > n
    return 2 if perfect_number?(n - k * k)
  end
  3
end

p num_squares(40901)

@hash = {}
def num_squares_mymethod(n)
  return @hash[n] if @hash.key?(n)
  return n if n <= 3
  k = Math.sqrt(n).to_i
  return 1 if k * k == n
  cands = k.downto(1).to_a
  res = n
  cands.each do |c|
    break if n / (c * c) > res
    x = 1
    x += 1 while x * c * c < n
    x -= 1
    res = [res, x + num_squares(n - x * c * c)].min
  end
  @hash[n] = res
  res
end

(0..100).each do |n|
  cache = [n, num_squares(n), num_squares_mymethod(n)]
  p cache if cache[1] != cache[2]
end
