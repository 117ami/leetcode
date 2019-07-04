
# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
#
# Note:
#
# sx, sy, tx, ty will all be integers in the range [1, 10^9].
# Discuss

# @param {Integer} sx
# @param {Integer} sy
# @param {Integer} tx
# @param {Integer} ty
# @return {Boolean}
def reaching_points(sx, sy, tx, ty)
  while sx <= tx && sy <= ty
    rate = 1
    if tx > ty
      rate <<= 1 while ty * rate + sx < tx
      rate >>= 1 if rate > 1
      tx -= ty * rate
    elsif ty > tx
      rate <<= 1 while tx * rate + sy < ty
      rate >>= 1 if rate > 1
      ty -= tx * rate
    else
      return sx == tx && sy == ty
    end
    return true if sx == tx && sy == ty
  end
  print "#{[sx, sy, tx, ty]} \n"
  tx == sx && ty == sy
end

p reaching_points(9, 10, 9, 19)
