# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# @param {Integer} n
# @return {Integer}
def count_primes(n)
  mark = [false] * (n + 1)
  count = 0
  (2..n-1).each do |i|
    next if mark[i]
    count += 1
    i * i.step(n, i) { |j| mark[j] = true }
  end
  count
end

def count_primes2(n)
  r = 0
  nonprime = {}
  (2..n - 1).each do |i|
    next if nonprime.key?(i)
    r += 1
    (2..n).each do |j|
      break if i * j > n
      nonprime[i * j] = nil
    end
  end
  r
end

n = 2
p count_primes(n)
# p count_primes2(n)
