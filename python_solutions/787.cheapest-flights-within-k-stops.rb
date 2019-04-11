#
# @lc app=leetcode id=787 lang=ruby
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (34.33%)
# Total Accepted:    35.8K
# Total Submissions: 104.2K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
#
#
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
#
# Note:
#
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
#
#
#
# @param {Integer} n
# @param {Integer[][]} flights
# @param {Integer} src
# @param {Integer} dst
# @param {Integer} k
# @return {Integer}

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# A native Priority Queue
class PriorityQueue
  def elements
    @es
  end

  def initialize
    @es = []
  end

  def <<(x)
    push(x)
  end

  def empty?
    @es.empty?
  end

  def pop
    @es.pop
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

def find_cheapest_price(n, edges, src, dst, k)
  prices = {}
  edges.each do |a, b, pr|
    prices[a] = { b => pr } unless prices.key?(a)
    prices[a][b] = pr
  end
  visited = (0..n).zip([0] * (n + 1)).to_h
  res = Float::INFINITY

  pq = PriorityQueue.new
  pq << [0, src, k + 1]
  until pq.empty?
    # p pq
    cp, cs, left = pq.pop
    # p [cp, cs, left]
    return cp if cs == dst

    visited[cs] = 1
    next unless left > 0 && prices.key?(cs)

    prices[cs].each_pair do |ns, pr|
      next if visited[ns] == 1

      pq << [cp + pr, ns, left - 1]
    end
  end
  -1
end

n = 3
edges = [[1, 0, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 1

n = 5
edges = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
src = 0
dst = 2
k = 2
p find_cheapest_price(n, edges, src, dst, k)
