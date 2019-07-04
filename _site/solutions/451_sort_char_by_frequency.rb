
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# @param {String} s
# @return {String}
def frequency_sort(s)
  fre = Hash.new(0).tap { |h| s.each_char { |c| h[c] += 1 } }
  r = ''
  fre.sort_by { |_, v| -v }.each { |c, n| r << c * n }
  # r << c * n is faster than Array.new(n, c).join, which is faster than n.times.each { r << c }
  r
end

s = 'd;lkajf;dkljs;afdk;jal;hfdlahfdlahfdaldhfuhfwouwiuiwyaohlqwehr'
s = 'aaAAAadafadfadassaaaa@@@@@dd'
s = 1_000_000.times.map { rand(65..90).chr }.join
# p s
frequency_sort(s)
