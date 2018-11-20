# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#  https://leetcode.com/problems/add-strings/description/
require './aux.rb'

# @param {String} num1
# @param {String} num2
# @return {String}
def add_strings(num1, num2)
  res = Array.new(5101, 0)
  num1, num2 = num2, num1 if num1.length > num2.length
  num1.reverse!
  num2.reverse!
  0.upto(num1.size - 1).each do |i|
    res[i] += num1[i].ord - 48 + num2[i].ord - 48
    res[i + 1] += (res[i] / 10)
    res[i] %= 10
  end
  num1.size.upto(num2.size - 1).each do |i|
    res[i] += num2[i].ord - 48
    res[i + 1] += (res[i] / 10)
    res[i] %= 10
  end
  res.pop while !res.empty? && res.last.zero?
  res.empty? ? '0' : res.reverse.join
end

num1 = '0'
num2 = '0'
p add_strings(num1, num2)
