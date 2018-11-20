#  Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

# @param {Integer} n
# @return {Integer}
def is_ugly(num)
  return true if num <= 3
  num /= 2 while num.even?
  num /= 3 while num % 3 == 0
  num /= 5 while num % 5 == 0
  num == 1
end

def brute_force(n)
  counter = 0
  (1..2 << 32).each do |i|
    counter += 1 if is_ugly(i)
    return i if counter == n
  end
end

def nth_ugly_number(n)
  init = [2, 3, 5]
  cache = {}
  i = 0
  loop do
    (0..i).each do |j|
      init << init[i] * init[j] unless cache.key?(init[i] * init[j])
      cache[init[i] * init[j]] = nil
    end
    i += 1
    break if init.size > n * 3
  end
  init.sort!
  init.unshift(1)
  init[n - 1]
end

def nth_ugly_number2(n)
  arr = [1]
  u1 = u2 = u3 = 0
  (1..n - 1).each do |i|
    arr[i] = [arr[u1] * 2, arr[u2] * 3, arr[u3] * 5].min
    u1 += 1 if arr[i] == arr[u1] * 2
    u2 += 1 if arr[i] == arr[u2] * 3
    u3 += 1 if arr[i] == arr[u3] * 5
  end
  arr.last
end

n = Random.rand(1..1000)
# n = 1690
p n
# p brute_force(n)
p nth_ugly_number(n)
p nth_ugly_number2(n)
