
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.

# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
def combination_sum3(k, n)
  return [] if n <= 0 || n > 45 || k < 1 || k > 9
  r = []
  Array(1..9).combination(k).each do |c|
    next if c[0] * k >= n # Adding this line makes the program 8ms faster
    r << c if c.reduce(:+) == n
  end
  r
end

nums = Array(1..9)
p combination_sum3(3, 45)
