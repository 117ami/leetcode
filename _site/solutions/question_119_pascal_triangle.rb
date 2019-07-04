
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# @param {Integer} row_index
# @return {Integer[]}
def get_row(row_index)
  res = [1]
  row_index.times do
    res = [[0] + res, res + [0]].transpose.map(&:sum)
  end
  res
end

p get_row(4)
