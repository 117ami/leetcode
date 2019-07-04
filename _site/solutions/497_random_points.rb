#
# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.
#
# Note:
#
# An integer point is a point that has integer coordinates.
# A point on the perimeter of a rectangle is included in the space covered by the rectangles.
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output:
# [null,[4,1],[4,1],[3,3]]
# Example 2:
#
# Input:
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output:
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
#
#

class Solution
  # :type rects: Integer[][]
  def initialize(rects)
    @aux = []
    @pointsum = 0
    rects.each_with_index do |r, _i|
      x1, y1, x2, y2 = r
      @pointsum += (x2 - x1 + 1) * (y2 - y1 + 1)
      @aux << [@pointsum, r]
    end
  end

  # :rtype: Integer[]
  def pick
    rn = rand(@pointsum)
    ridx = (0..@aux.size - 1).bsearch { |j| rn < @aux[j].first }
    [rand(@aux[ridx][1][0]..@aux[ridx][1][2]), rand(@aux[ridx][1][1]..@aux[ridx][1][3])]
  end
end

# Your Solution object will be instantiated and called as such:
rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]
# rects = [[82_918_473, -57_180_867, 82_918_476, -57_180_863], [83_793_579, 18_088_559, 83_793_580, 18_088_560], [66_574_245, 26_243_152, 66_574_246, 26_243_153], [72_983_930, 11_921_716, 72_983_934, 11_921_720]]
obj = Solution.new(rects)
p obj.pick
