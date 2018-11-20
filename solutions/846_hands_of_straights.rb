# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
#
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.

# @param {Integer[]} hand
# @param {Integer} w
# @return {Boolean}
def is_n_straight_hand(hand, w)
  return false unless hand.size % w == 0
  counts = Hash.new(0).tap { |h| hand.sort.each { |n| h[n] += 1 } }
  loop do
    return true if counts.empty?
    a = []
    while a.size < w
      #p [a, counts]
      xn = a.empty? ? counts.first[0] : a[-1] + 1
      return false unless counts.key?(xn)
      counts[xn] -= 1
      counts.delete(xn) if counts[xn].zero?
      a << xn
    end
  end
  counts.empty?
end

hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
w = 3
p is_n_straight_hand(hand, w)
