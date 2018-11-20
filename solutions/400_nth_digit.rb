# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

# @param {Integer} n
# @return {Integer}
def find_nth_digit(n)
  s = [1, 1]
  while n > s[1]
    s[0] += 1
    s[1] += s[0].to_s.length
  end
  s[0].to_s[n - s[1] - 1]
end

def find_nth_digit2(n)
  return n if n < 10
  cache = [[1, 9, 9], [2, 99, 189], [3, 999, 2889], [4, 9999, 38_889], [5, 99_999, 488_889], [6, 999_999, 5_888_889],
           [7, 9_999_999, 68_888_889], [8, 99_999_999, 788_888_889], [9, 999_999_999, 8_888_888_889]]
  i = 0
  i += 1 while cache[i].last < n
  return cache[i][1].to_s[-1].to_i if cache[i].last == n

  quo = (n - cache[i - 1][-1]) / cache[i][0]
  rem = (n - cache[i - 1][-1]) % cache[i][0]
  return (quo + cache[i - 1][1]).to_s[-1].to_i if rem.zero?
  (quo + cache[i - 1][1] + 1).to_s[rem - 1].to_i
end

(1..10).each do |n|
  p find_nth_digit(n)
end
p 2**31 - 1

10.times.each do |_i|
  n = Random.rand(2**10 - 1)
  n = 38_889
  p [n, find_nth_digit(n), find_nth_digit2(n)]
end
