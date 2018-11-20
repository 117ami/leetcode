# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.

# @param {String} s
# @return {Integer}
def count_binary_substrings(s)
  c = s[0]
  ret = i = j = 0
  s.each_char do |b|
    if c == b
      i += 1
    else
      ret += [i, j].min
      j = i
      i = 1
      c = b
    end
  end
  ret += [i, j].min
end

s = '10101'
p count_binary_substrings(s)
