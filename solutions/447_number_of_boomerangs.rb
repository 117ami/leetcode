# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
# Output:
# 2
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#

# @param {Integer[][]} points
# @return {Integer}
def number_of_boomerangs(points)
  res = 0
  points.each do |p|
    boom = Hash.new(0)
    points.each do |q|
      a = p[0] - q[0]
      b = p[1] - q[1]
      d = a * a + b * b
      boom[d] += 1
    end
    boom.each_value { |v| res += v * (v - 1) }
  end
  res
end
