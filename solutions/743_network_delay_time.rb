#
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K.  How long will it take for all nodes to receive the signal?  If it is impossible, return -1.
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
#
#  https://leetcode.com/problems/network-delay-time/description/
require './aux.rb'

# @param {Integer[][]} times
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def network_delay_time(argtimes, n, k)
  dist = [Float::INFINITY] * (n + 1)
  dist[k] = 0
  n.times do
    argtimes.each do |u, v, dur|
      dist[v] = dist[u] + dur if dist[u] < Float::INFINITY && dist[v] > dist[u] + dur
    end
  end
  res = dist[1..-1].max
  res == Float::INFINITY ? -1 : res
end

argtimes = [[1, 2, 10], [2, 4, 23], [4, 3, 100], [3, 1, 29]]
n = 4
k = 2
p network_delay_time(argtimes, n, k)
