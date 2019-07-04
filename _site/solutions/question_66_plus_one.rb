#!/usr/bin/ruby -w

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.

# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
  (digits.join.to_i + 1).to_s.split('').map(&:to_i)
end

def plus_one_2(digits)
  vals = []
  # The || used here in case of digits is empty: digits.pop = nil 
  vals << 0 while (memo = (digits.pop || 0) + 1) == 10
  digits + Array(memo) + vals
end

digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# digits = [9, 9, 9, 9, 9]
p plus_one(digits)
p plus_one_2(digits)

