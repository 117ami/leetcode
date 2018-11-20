# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
  return [] if num_rows.zero?
  res = [[1]]
  (2..num_rows).map { res << [[0] + res[-1], res[-1] + [0]].transpose.map(&:sum) }
  res
end

p generate(5)
