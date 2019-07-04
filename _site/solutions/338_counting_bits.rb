
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# @param {Integer} num
# @return {Integer[]}
#  Follow up:
#
#     It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
#     Space complexity should be O(n).
#     Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#

def count_bits(num)
  (0..num).map { |i| i.to_s(2).count('1') }
end

def count_bits_2(num)
  base = [0]
  (0..base.size - 1).each { |i| base << base[i] + 1 } while base.size < num + 1
  base[0..num]
end

(0..32).each do |i|
  p count_bits(i)
  p count_bits_2(i)
end
