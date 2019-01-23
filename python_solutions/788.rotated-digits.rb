#
# @lc app=leetcode id=788 lang=ruby
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (52.17%)
# Total Accepted:    20.8K
# Total Submissions: 39.6K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
#
#
# Note:
#
#
# N  will be in range [1, 10000].
#
#
#
# @param {Integer} n
# @return {Integer}
def rotated_digits2(n)
  memo = { 0 => 'almost' }
  isgood = lambda do |k|
    m, n = k.divmod(10)
    memo[k] = if n == 3 || n == 4 || n == 7 || memo[m] == 'bad'
                'bad'
              elsif (n == 0 || n == 1 || n == 8) && memo[m] == 'almost'
                'almost'
              else
                'good'
              end
  end
  1.upto(n).map { |k| isgood.call(k) }.count('good')
end

def rotated_digits(n)
	ans = 0
	dp = [0] * (n + 1)
	dp[0..9] = [1, 1, 2, 0, 0, 2, 2, 0, 1, 2] 
	0.upto(n).each do |k|
		a, b = dp[k / 10], dp[k % 10]
		next if a.zero? || b.zero?
		dp[k] = 1 if a == 1 && b == 1
		next if a + b == 2
		dp[k] = 2
		ans += 1
	end
	ans 
end

p rotated_digits(857)

