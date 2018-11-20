
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# Example 1:
# n = 5
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# Because the 3rd row is incomplete, we return 2.
# Example 2:
# n = 8
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# Because the 4th row is incomplete, we return 3.

# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
  i = 1
  i += 1 while (i + 1) * i / 2 <= n
  i - 1
end

def arrange_coins2(n)
  res = Math.sqrt(n * 2).to_i
  res -= 1 if (res + 1) * res / 2 > n
  res
end

p arrange_coins(2**32 - 1)

(1..1_000_000).each do |i|
  arrange_coins2(i)
  # p [i, arrange_coins(i), arrange_coins2(i)] unless arrange_coins2(i) == arrange_coins(i)
end
