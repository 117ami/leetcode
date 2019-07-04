#
# An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.
# Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.
# Example 1:
# Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# Output: 3
# Explanation:
# Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
# Also, there isn't a smaller size set that fulfills the above condition.
# Thus, we output the size of this set, which is 3.
# Example 2:
# Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# Output: 5
# Explanation:
# An example of a minimum sized set is {1, 2, 3, 4, 5}.
# Note:
# intervals will have length in range [1, 3000].
# intervals[i] will have length 2, representing some integer interval.
# intervals[i][j] will be an integer in [0, 10^8].
#
#  https://leetcode.com/problems/set-intersection-size-at-least-two/description/

# @param {Integer[][]} intervals
# @return {Integer}
def intersection_size_two(intervals)
  intervals.sort_by!(&:first).reverse!.sort_by!(&:last)
  p intervals
  res = 0
  pa = pb = -1
  visited = Hash.new(0)
  intervals.each do |a, b|
    next if a <= pa
    if a > pb
      res += 2
      pb = b
      pa = b - 1
    else
      res += 1
      pa = pb
      pb = b
    end
    visited[pa] += 1
    visited[pb] += 1
    p [a, b, res, pa, pb]
  end
  p visited.keys
  res
end

intervals = [[2, 3], [1, 3], [1, 4], [2, 5], [3, 5]]
intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
intervals = [[16, 18], [11, 18], [15, 23], [1, 16], [10, 16], [6, 19], [18, 20], [7, 19],
             [10, 11], [11, 23], [6, 7], [23, 25], [1, 3], [7, 12], [1, 13], [23, 25], [10, 22], [23, 25],
             [0, 19], [0, 13], [7, 12], [14, 19], [8, 17], [7, 23], [4, 24]]
#intervals = [[0, 1], [1, 3], [1, 2]]
#intervals = [[4,7],[5,8],[7,9],[2,6],[0,1],[1,4],[1,9],[0,5],[5,10],[7,8]]
p intersection_size_two(intervals)
