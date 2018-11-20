# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can chooseX >= 2 such thatit is possible to split the entire deckinto 1 or more groups of cards, where:
#   Each group has exactly X cards.
#   All the cards in each group have the same integer.
#
# Example 1:
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# Example 2:
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# Example 3:
# Input: [1]
# Output: false
# Explanation: No possible partition.
# Example 4:
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# Example 5:
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
# Note:
#   1 <= deck.length <= 10000
#   0 <= deck[i] <10000
#
#  https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
require './aux.rb'

# @param {Integer[]} deck
# @return {Boolean}
def has_groups_size_x(deck)
  szs = deck.group_by(&:itself).values.map(&:size).sort
  return false if szs[0] < 2
  p szs
  2.upto(szs[0]).each do |k|
    res = true
    szs.each do |n|
      if n % k != 0
        res = false
        break
       end
    end
    return true if res == true
  end
  false
end

deck = [1, 1, 2, 2, 2, 2]
deck = [1, 2, 3, 4, 4, 3, 2, 1]
deck = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
deck = [1, 1, 1, 2, 2, 2, 3, 3]
p has_groups_size_x(deck)
