# Given an array of unique integers, each integer is strictly greater than 1.
# We make a binary tree using these integersand each number may be used for any number of times.
# Each non-leaf node'svalue should be equal to the product of the values of it's children.
# How many binary trees can we make? Return the answer modulo 10 ** 9 + 7.
# Example 1:
# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:
# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
# Note:
#   1 <= A.length <=1000.
#   2 <=A[i]<=10 ^ 9.
#
#  https://leetcode.com/problems/binary-trees-with-factors/description/
require './aux.rb'
require 'prime'

# @param {Integer[]} a
# @return {Integer}
def num_factored_binary_trees(a)
  a.sort!
  poss = { a[0] => 1 }
  res = 1
  a[1..-1].each_with_index do |n, idx|
    idx += 1
    cur = 1
    0.upto(idx - 1).each do |jdx|
      if n % a[jdx] == 0 && poss.key?(n / a[jdx])
        cur += poss[a[jdx]] * poss[n / a[jdx]]
      end
    end
    res += cur
    poss[n] = cur
  end
  res % (10**9 + 7)
end

def factors(n)
  pd = n.prime_division.map { |pd| (0..pd[1]).map { |i| pd[0]**i } }
  pd.length == 1 ? pd[0] : pd[0].product(*pd.drop(1)).map { |a| a.reduce(:*) }.sort
end

a = [2, 4, 10, 5]
p num_factored_binary_trees(a)
