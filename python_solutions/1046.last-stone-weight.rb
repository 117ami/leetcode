#
# @lc app=leetcode id=1046 lang=ruby
#
# [1046] Last Stone Weight
#
# https://leetcode.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (64.22%)
# Total Accepted:    5.1K
# Total Submissions: 7.9K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of rocks, each rock has a positive integer weight.
#
# Each turn, we choose the two heaviest rocks and smash them together.  Suppose
# the stones have weights x and y with x <= y.  The result of this smash
# is:
#
#
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
#
#
# At the end, there is at most 1 stone left.  Return the weight of this stone
# (or 0 if there are no stones left.)
#
#
#
# Example 1:
#
#
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the
# value of last stone.
#
#
#
# Note:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
# @param {Integer[]} stones
# @return {Integer}

# A native Priority Queue
class PriorityQueue
  def elements
    @es
  end

  def initialize
    @es = []
  end

  def size
    @es.size
  end

  def empty?
    @es.empty?
  end

  def <<(x)
    push(x)
  end

  def pop
    @es.pop
  end

  def shift
    @es.shift
  end

  def push(x) # x is assumed to be an integer or a string
    return pusharray(x) if x.is_a?(Array)

    idx = (0..@es.size - 1).bsearch { |i| @es[i] < x } || @es.size
    @es.insert(idx, x)
  end

  def pusharray(x) # x is assumed to be an array
    idx = (0..@es.size - 1).bsearch { |i| @es[i].first <= x.first } || @es.size
    @es.insert(idx, x)
  end
end

def last_stone_weight(stones)
  pq = PriorityQueue.new
  stones.each { |c| pq.push(c) }
  pq.push(pq.shift - pq.shift) while pq.size > 1
  return 0 if pq.empty?

  pq.pop
end

stones = [2, 7, 4, 1, 8]
p last_stone_weight(stones)
