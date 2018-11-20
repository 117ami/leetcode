# Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10n.
#     Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])
# Credits:Special thanks to @memoryless for adding this problem and creating all test cases.

# @param {Integer} n
# @return {Integer}
def count_numbers_with_unique_digits(n)
  return 1 if n.zero?
  return count_numbers_with_unique_digits(10) if n > 10
  base = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  base[0..n - 1].reduce(:*) + count_numbers_with_unique_digits(n - 1)
end

p count_numbers_with_unique_digits(10)
