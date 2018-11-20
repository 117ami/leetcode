# Given an array A, partition itinto two (contiguous) subarraysleftand rightso that:
#   Every element in leftis less than or equal to every element in right.
#   left and right are non-empty.
#   lefthas the smallest possible size.
# Return the length of left after such a partitioning. It is guaranteed that such a partitioning exists.
#
# Example 1:
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
# Note:
#   2 <= A.length<= 30000
#   0 <= A[i] <= 10^6
#   It is guaranteed there is at least one way to partition A as described.
#
#  https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
require './aux.rb'

# @param {Integer[]} a
# @return {Integer}
def partition_disjoint(a)
  cter = Hash.new(0).tap { |h| a.each { |n| h[n] += 1 } }
  cter = cter.sort.to_h
  leftmax = a.first
  rightmin = 10**7
  a.each_with_index do |n, idx|
    leftmax = [leftmax, n].max
    cter[n] -= 1
    cter.delete(n) if cter[n].zero?
    rightmin = cter.first.first
    # p [idx, n, cter, rightmin]
    return idx + 1 if rightmin >= leftmax
  end
end

a = [1, 1, 1, 0, 6, 12]
a = random_list(6, 100)
h = { 2 => 1 }

p a
p partition_disjoint(a)
