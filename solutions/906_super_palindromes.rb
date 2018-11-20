# Let's say a positive integer is asuperpalindromeif it is a palindrome, and it is also the square of a palindrome.
# Now, given two positiveintegers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].
#
# Example 1:
# Input: L = "4", R = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
#
# Note:
#   1 <= len(L) <= 18
#   1 <= len(R) <= 18
#   L and R are strings representing integers in the range [1, 10^18).
#   int(L) <= int(R)
#
#  https://leetcode.com/problems/super-palindromes/description/
require './aux.rb'

# @param {String} l
# @param {String} r
# @return {Integer}
def superpalindromes_in_range(l, r)
  na, nb = [l, r].map { |k| Math.sqrt(k.to_i).to_i }
  sa, sb = [na, nb].map(&:to_s).map(&:length)
  res = 0
  sa.upto(sb).each do |len|
    createP(len).each do |sn|
      next if sn[0] == '0'
      n = sn.to_i
      res += 1 if n >= na && n <= nb && isP?((n * n).to_s)
    end
  end
  res
end

l = '4'
r = '1001'
p superpalindromes_in_range(l, r)
