# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
#
# Example:
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Note:
#
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.

# @param {String} start
# @param {String} end
# @return {Boolean}
def can_transform(start, ends)
  return false unless start.delete('X') == ends.delete('X')

  idx = lambda do |s, c|
    r = Array(0..s.length - 1).keep_if { |i| s[i] == c }
  end

  ls = idx.call(start, 'L')
  le = idx.call(ends, 'L')
  return false if ls.pop < le.pop until ls.empty?

  ls = idx.call(start, 'R')
  le = idx.call(ends, 'R')
  return false if ls.pop > le.pop until ls.empty?

  true
end

s = 'RXXLRXRXL'
e = 'XRLXXRRLX'
p can_transform(s, e)
