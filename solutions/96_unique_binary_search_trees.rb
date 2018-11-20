# Given n, how many structurally unique BST's (binary search trees) that store values 1 ...n?
# Example:
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#  https://leetcode.com/problems/unique-binary-search-trees/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def num_trees(n)
  return n if n <= 2
  cache = [1, 1, 2]
  3.upto(n).each do |k|
    cache[k] = 0.upto(k - 1).map { |i| cache[i] * cache[k - i - 1] }.reduce(:+)
  end
  cache.last
end

n = 9
p num_trees(n)
