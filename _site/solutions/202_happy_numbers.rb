# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# @param {Integer} n
# @return {Boolean}
def is_happy(n)
  return true if n == 1
  cache = {} # n => nil}
  loop do
    break if cache.key?(n)
    cache[n] = nil
    m = 0
    until n.zero?
      m += (n % 10) * (n % 10)
      n /= 10
    end
    return true if m == 1
    n = m
  end
  false
end

def is_happy_2(n)
  cache = {}
  loop do
    break if cache.key?(n)
    return true if n == 1
    cache[n] = nil
    m = n.to_s.chars.map(&:to_i).reduce(0) { |ssum, i| ssum += i * i }
    n = m
  end
  false
end

(1..20).each do |i|
  p [i, is_happy(i), is_happy_2(i)]
end
