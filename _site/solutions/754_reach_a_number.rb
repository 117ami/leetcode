#  You are standing at position 0 on an infinite number line. There is a goal at position target.
#
# On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
#
# Return the minimum number of steps required to reach the destination.
#
# Example 1:
#
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
#
# Example 2:
#
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
#
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].

# @param {Integer} target
# @return {Integer}
def reach_number(target)
  return reach_number(target * -1) if target < 0
  n = Math.sqrt(target).ceil
  n += 1 while (n + 1) * n / 2 < target || ((n + 1) * n / 2 - target).odd?
  n
end

(1..69).each do |i|
  # print [i, reach_number(i)], "  "
  print i, ' ', reach_number(i), ' ** '
end
target = 90_202_021
p reach_number(target)
