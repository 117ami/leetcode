
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.

# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  r = 0
  maxh = 0
  idx = {}

  heights.each_with_index do |h, i|
    idx[h] = i unless idx.key?(h)
    if h > maxh
      maxh = h
      next
    end

    idx.each_pair do |k, v|
      next unless k > h
      r = [r, k * (i - v)].max
      idx[h] = [idx[h], v].min
      idx.delete(k)
    end

    maxh = h
  end

  idx.each { |k, v| r = [r, (heights.size - v) * k].max }
  r
end

def largest_rectangle_area_2(heights)
  return 0 if heights.empty?
  heights << 0
  stack = [-1]
  r = 0
  heights.each_with_index do |h, i|
    while !stack.empty? && heights[stack[-1]] > h
      r = [r, heights[stack.pop] * (i - stack[-1] - 1)].max
    end
    stack.push(i)
  end
  r
end

heights = [2, 1, 5, 6, 2, 3]
heights = [2, 2, 3, 3, 3, 1, 0, 1, 3, 4, 3, 1, 2]
heights = [4, 2, 0, 3, 2, 5]
# heights = [0, 0, 0, 2147483647]
p largest_rectangle_area_2(heights)
