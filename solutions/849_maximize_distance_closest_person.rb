# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:
#
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.

# @param {Integer[]} seats
# @return {Integer}
def max_dist_to_closest(seats)
  avail = seats.each_with_index.select { |v, i| i if v == 1 }.map(&:reverse).to_h
  xmax = 0
  akeys = avail.keys
  return [akeys[0], seats.size - 1 - akeys[0]].max if akeys.size == 1
  akeys.each_with_index do |k, i|
    if i.zero?
      xmax = k if k > 0
    elsif
      mid = (k + akeys[i - 1]) / 2
      xmax = [xmax, [mid - akeys[i - 1], k - mid].min].max
      xmax = [xmax, [1 + mid - akeys[i - 1], k - mid - 1].min].max
      xmax = [xmax, seats.size - 1 - k].max if i == akeys.size - 1
    end
  end
  xmax
end

seats = [1, 0, 0, 0, 1, 0, 1]
# seats = [1, 0, 0, 0]
# seats = [1, 0, 1]
p max_dist_to_closest(seats)
