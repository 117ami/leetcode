# For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.
# Now given a string representing n, you should return the smallest good base of n in string format.
# Example 1:
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
# Example 2:
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
# Example 3:
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# Note:
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading zeros.
#
#  https://leetcode.com/problems/smallest-good-base/description/
require './aux.rb'

# @param {String} n
# @return {String}
def smallest_good_base(n)
  n = n.to_i
  maxe = Math.log(n + 1, 2).round
  base = 1
  maxe.downto(1).each do |e|
    base = (n**e**-1).to_i
    base = n - 1 if e == 1
    next if base == 1
    # p [e, base]
    return base.to_s if (base**(e + 1) - 1) / (base - 1) == n
  end
end

n = 1_000_000_000_000_000_000
# n = 4681
p smallest_good_base(n)
