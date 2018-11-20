# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
#
# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two rectangles, return whether they overlap.

# @param {Integer[]} rec1
# @param {Integer[]} rec2
# @return {Boolean}
def is_rectangle_overlap1(rec1, rec2)
  return is_rectangle_overlap(rec2, rec1) if rec1[0] > rec2[0]
  return false if rec2[0] >= rec1[2] ||
                  rec2[1] >= rec1[3] ||
                  rec1[1] >= rec2[3]
  true
end

rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]

rec1 = [5,15,8,18]
rec2 = [0,3,7,9]

rec1 = [-5,8,0,8]
rec2 = [-5,4,5,5]

rec1 = [4,4,14,7]
rec2 = [4,3,8,8]
p is_rectangle_overlap(rec1, rec2)

