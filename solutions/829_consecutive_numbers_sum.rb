# Given a positive integerN, how many ways can we write it as a sum ofconsecutive positive integers?
# Example 1:
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note:1 <= N <= 10 ^ 9.

# @param {Integer} n
# @return {Integer}
def consecutive_numbers_sum(n)
  ans = 1
  (2..Math.sqrt(2 * n)).each do |k|
    ans += 1 if (n - (k - 1) * k / 2) % k == 0
  end
  ans
end

p consecutive_numbers_sum(15)
