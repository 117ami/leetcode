# Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
#
# Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
#
# Example 1:
#
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
#
# Return true. All 5 rectangles together form an exact cover of a rectangular region.
# They can not overlap each other too.

# @param {Integer[][]} rectangles
# @return {Boolean}
# 1) One rectangle is above top edge of other rectangle.
# 2) One rectangle is on left side of left edge of other rectangle.
def overlap?(b1, b2)
  return false if b1[0] >= b2[2] || b2[0] >= b1[2]
  return false if b1[1] >= b2[3] || b2[1] >= b1[3]
  true
end

def area(b)
  (b[2] - b[0]) * (b[3] - b[1])
end

def update_corners(h, k)
  h.key?(k) ? h.delete(k) : h[k] = nil
end

def is_rectangle_cover(rectangles)
  mina, minb, maxa, maxb = rectangles[0]
  totalarea = 0
  h = {}
  rectangles.each do |b|
    mina = [b[0], mina].min
    minb = [b[1], minb].min
    maxa = [b[2], maxa].max
    maxb = [b[3], maxb].max
    totalarea += area(b)
    update_corners(h, [b[0], b[1]].join)
    update_corners(h, [b[2], b[1]].join)
    update_corners(h, [b[0], b[3]].join)
    update_corners(h, [b[2], b[3]].join)
  end
  return false unless h.keys.size == 4 &&
                      h.key?([mina, minb].join) &&
                      h.key?([maxa, minb].join) &&
                      h.key?([mina, maxb].join) &&
                      h.key?([maxa, maxb].join)
  totalarea == area([mina, minb, maxa, maxb])
end

rectangles = [
  [1, 1, 3, 3],
  [3, 1, 4, 2],
  [3, 2, 4, 4],
  [1, 3, 2, 4],
  [2, 3, 3, 4]
]

rectangles = [[0, 0, 4, 1], [7, 0, 8, 2], [6, 2, 8, 3], [5, 1, 6, 3], [4, 0, 5, 1], [6, 0, 7, 2], [4, 2, 5, 3], [2, 1, 4, 3], [0, 1, 2, 2], [0, 2, 2, 3], [4, 1, 5, 2], [5, 0, 6, 1]]

rectangles = [[0, 0, 1, 1], [0, 1, 3, 2], [1, 0, 2, 2]]
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]

p is_rectangle_cover(rectangles)
