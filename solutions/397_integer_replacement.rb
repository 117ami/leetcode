#
# Given a positive integer n and you can do operations as follow:
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?
# Example 1:
# Input:
# 8
# Output:
# 3
# Explanation:
# 8 -> 4 -> 2 -> 1
# Example 2:
# Input:
# 7
# Output:
# 4
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
# @param {Integer} n
# @return {Integer}
def integer_replacement(n)
  counter = 0
  while n > 1
    if n.even?
      n /= 2
    elsif (n + 1) % 4 == 0 && n != 3
      n += 1
    else
      n -= 1
    end
    counter += 1
  end
  counter
end

def integer_replacement2(n)
  seen = { 1 => 0, 2 => 1 }
  helper = lambda do |i|
    return seen[i] if seen.key?(i)
    seen[i] = if i.even?
                1 + helper.call(i / 2)
              else
                1 + [helper.call(i - 1), helper.call(i / 2 + 1) + 1].min
              end
    seen[i]
  end
  helper.call(n)
end

n = 10_000_000
p integer_replacement(n)
p integer_replacement2(n)

(1..10).each { |i| p [i, integer_replacement(i)] }
