#
# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].
#
#  https://leetcode.com/problems/2-keys-keyboard/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def min_steps2(n)
  return 0 if n == 1
  res = Array(1..n)
  res.unshift(0)
  1.upto(n / 2).each do |i|
    j = 2
    while i * j <= n
      res[i * j] = [res[i * j], res[i] + j].min
      j += 1
    end
  end
  res[n]
end

def min_steps(n)
  return 0 if n == 1
  return n if n <= 5
  k = 2
  k += 1 while n % k != 0
  return n if k == n
  min_steps(n / k) + k
end

1.upto(100).each do |n|
  p [n, min_steps(n), min_steps2(n)]
end
