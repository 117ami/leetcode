# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#

# @param {String} s
# @param {Character} c
# @return {Integer[]}
def shortest_to_char(s, c)
  ret = []
  locations = (0..s.size - 1).select { |i| s[i] == c }
  ret.push(*Array(0..locations[0]).reverse)
  l = locations[0]
  locations.each do |r|
    (l + 1..r).each do |j|
      ret << [j - l, r - j].min
    end
    l = r
  end
  ret.push(*Array(1..s.size - 1 - locations[-1])) if locations[-1] < s.size - 1
  ret
end

p shortest_to_char('aaba', 'b')
