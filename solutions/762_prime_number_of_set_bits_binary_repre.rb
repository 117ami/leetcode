#  Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
#
# (Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

# @param {Integer} l
# @param {Integer} r
# @return {Integer}

def count_prime_set_bits(l, r)
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31].zip([]).to_h
  (l..r).select { |n| primes.key?(n.to_s(2).count('1')) }.size
end

p count_prime_set_bits(10, 15)
