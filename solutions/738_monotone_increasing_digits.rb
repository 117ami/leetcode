#
# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note:
# N is an integer in the range [0, 10^9].
#

# @param {Integer} n
# @return {Integer}
def monotone_increasing_digits(n)
  nstr = n.to_s.chars.map(&:to_i)
  loc = nstr.size + 1
  (nstr.size - 1).downto(1).each do |i|
    next if nstr[i] >= nstr[i - 1]
    nstr[i - 1] -= 1
    loc = i
  end
  loc.upto(nstr.size - 1).each { |i| nstr[i] = '9' }
  nstr.join.to_i
end

n = 5_666_661
p monotone_increasing_digits(n)
