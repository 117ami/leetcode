#
# @lc app=leetcode id=886 lang=ruby
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (40.63%)
# Total Accepted:    13.2K
# Total Submissions: 32.6K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the
# same group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups
# in this way.
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
# Example 1:
#
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
#
#
# Example 2:
#
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
#
# Example 3:
#
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
#
# Note:
#
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
#
#
#
#
#
#
# @param {Integer} n
# @param {Integer[][]} dislikes
# @return {Boolean}

def find(parent, n)
  return n if n == parent[n]

  parent[n] = find(parent, parent[n])
  parent[n]
end

def possible_bipartition(n, dislikes)
  parents = (0..n).to_a
  m = {}
  dislikes.each do |a, b|
    m[a] = [] unless m.key?(a)
    m[a] << b
    m[b] = [] unless m.key?(b)
    m[b] << a
  end

  1.upto(n).each do |i|
    next unless m.key?(i)

    p1 = find(parents, i)
    p2 = find(parents, m[i].first)
    return false if p1 == p2

    m[i][1..-1].each do |j|
      pj = find(parents, j)
      return false if p1 == pj

      parents[j] = p2
    end
  end
  true
end

n = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
n = 5
dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
p possible_bipartition(n, dislikes)
