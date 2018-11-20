# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
# The coordinate (x,y) of a point is represented by an integer array with two integers.
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#  Note:
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.
#

# @param {Integer[]} p1
# @param {Integer[]} p2
# @param {Integer[]} p3
# @param {Integer[]} p4
# @return {Boolean}
def valid_square(p1, p2, p3, p4)
  s = [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]].map { |a, b| dis(a, b) }.uniq
  s.size == 2 && s.count(0).zero?
end

def dis(a, b)
  # distance between points a and b
  (a[0] - b[0])**2 + (a[1] - b[1])**2
end

p 3**3
