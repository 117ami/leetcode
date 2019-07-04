
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

# @param {Integer[][]} triangle
# @return {Integer}
def minimum_total(triangle)
  (triangle.size - 2).downto(0).each do |i|
    (0..triangle[i].size - 1).each { |j| triangle[i][j] += [triangle[i + 1][j], triangle[i + 1][j + 1]].min }
  end
  triangle[0][0]
end

triangle = [
  [2],
  [3, 4],
  [6, 5, 7],
  [4, 1, 8, 3]
]

p minimum_total(triangle)
