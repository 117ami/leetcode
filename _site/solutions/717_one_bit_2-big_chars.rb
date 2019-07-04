# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
#
# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
# Note:
#
# 1 <= len(bits) <= 1000.
# bits[i] is always 0 or 1.

# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
  return true if bits.size < 2 || bits[-2].zero?
  i = 0
  while i < bits.size - 1
    i += if bits[i].zero?
           1
         else
           2
         end
  end
  return false if i == bits.size
  true
end

a = 10.times.map { Random.rand(2) }
a << 0
p a
p is_one_bit_character(a)
