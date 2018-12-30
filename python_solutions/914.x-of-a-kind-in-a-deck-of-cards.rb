#
# @lc app=leetcode id=914 lang=ruby
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (33.98%)
# Total Accepted:    10.7K
# Total Submissions: 31.6K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
#
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
#
#
# Example 1:
#
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 3:
#
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 4:
#
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
#
#
#
# Example 5:
#
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
#
#
#
#
#
#
#
# Note:
#
#
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
#
#
#
#
#
#
#
#
#
#
#
#
#
# @param {Integer[]} deck
# @return {Boolean}
def has_groups_size_x(deck)
  # gcd = lambda do |a, b|
  #   b == 0 ? a : gcd.call(b, a % b)
  # end
  value_counts = deck.group_by(&:itself).values.map(&:size)
  x = value_counts.min
  value_counts.each do |v|
    x = v.gcd(x)
    return false if x == 1
  end
  true
end
	
deck = [1, 1, 1, 2, 2, 2, 3, 3, 3]
p has_groups_size_x(deck)
