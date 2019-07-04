# require './aux.rb'
# @param {Integer[][]} a
# @return {Integer}
def shortest_bridge(a)
  found = 0
  0.upto(a.size - 1).each do |i|
    0.upto(a.size - 1).each do |j|
      found = paint(a, i, j)
      break unless found.zero?
    end
    break unless found.zero?
  end

  2.upto(1000).each do |cl|
    0.upto(a.size - 1).each do |i|
      0.upto(a.size - 1).each do |j|
        return cl - 2 if a[i][j] == cl &&
                         (expand(a, i - 1, j, cl) || expand(a, i + 1, j, cl) ||
                           expand(a, i, j - 1, cl) || expand(a, i, j + 1, cl))
      end
    end
  end
end

def expand(a, i, j, cl)
  return false if i < 0 || j < 0 || i == a.size || j == a.size

  a[i][j] = cl + 1 if a[i][j].zero?
  a[i][j] == 1
end

def paint(a, i, j)
  return 0 if i < 0 || j < 0 || i == a.size || j == a.size || a[i][j] != 1

  a[i][j] = 2
  1 + paint(a, i - 1, j) + paint(a, i + 1, j) + paint(a, i, j - 1) + paint(a, i, j + 1)
end

# a = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
# p shortest_bridge(a)

# [934] Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/description/
# * algorithms
# * Medium (41.47%)
# * Total Accepted:    3.5K
# * Total Submissions: 8.5K
# * Testcase Example:  '[[0,1],[1,0]]'
# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
# Example 1:
# Input: [[0,1],[1,0]]
# Output: 1
# Example 2:
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# Note:
#   1 <= A.length = A[0].length <= 100
#   A[i][j] == 0 or A[i][j] == 1
