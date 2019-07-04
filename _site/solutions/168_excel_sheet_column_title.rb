# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
# Input: 1
# Output: "A"
# Example 2:
# Input: 28
# Output: "AB"
# Example 3:
# Input: 701
# Output: "ZY"
#

# @param {Integer} n
# @return {String}
def convert_to_title(n)
  n == 0 ? '' : convert_to_title((n - 1) / 26) + ((n - 1) % 26 + 'A'.ord).chr
end

p (1 + 'A'.ord).chr

1.upto(55).each do |i|
  p [i, convert_to_title(i)]
end
