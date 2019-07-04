# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note:
# The input number n will not exceed 100,000,000. (1e8)
#

# @param {Integer} num
# @return {Boolean}
def check_perfect_number(num)
  return false if num <= 1
  xsum = 1
  (2..Math.sqrt(num)).each do |i|
    next unless num % i == 0
    xsum += (num / i) + i
  end
  xsum == num
end

(1..3000).each do |i|
  p i if check_perfect_number(i)
end

n = 100_000_000
p check_perfect_number(n)
