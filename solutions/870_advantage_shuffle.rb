# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices ifor which A[i] > B[i].
# Return any permutation of A that maximizes its advantage with respect to B.
#
# Example 1:
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
#
# Note:
#   1 <= A.length = B.length <= 10000
#   0 <= A[i] <= 10^9
#   0 <= B[i] <= 10^9
#
#  https://leetcode.com/problems/advantage-shuffle/description/
require './aux.rb'

# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def advantage_count(a, b)
  b = Array(0..b.size - 1).map { |idx| [b[idx], idx] }.sort_by(&:first)
  a = Array(0..a.size - 1).map { |idx| [a[idx], idx] }.sort_by(&:first)
  res = []
  i = j = 0
  allidxs = (0..a.size - 1).zip([nil]).to_h
  while j < a.size
    if b[i].first < a[j].first
      res << [a[j].first, b[i].last]
      allidxs.delete(b[i].last)
      i += 1
      j += 1
    else
      res << [a[j].first, -1]
      j += 1
    end
  end
  indexes = allidxs.keys
  res.map { |n, i| i == -1 ? [n, indexes.pop] : [n, i] }.sort_by(&:last).map(&:first)
end

a = [2, 7, 11, 15]
b = [1, 10, 4, 11]

a = [2, 0, 4, 1, 2]
b = [1, 3, 0, 0, 2]

p advantage_count(a, b)
