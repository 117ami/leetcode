# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# @param {String} num1
# @param {String} num2
# @return {String}
def multiply(num1, num2)
  arr1 = num1.chars.reverse.map(&:to_i)
  arr2 = num2.chars.reverse.map(&:to_i)
  return 0 if arr1[-1].zero? || arr2[-1].zero?
  res = Array.new(arr1.size + arr2.size, 0)

  0.upto(arr1.size - 1) do |i|
    0.upto(arr2.size - 1) do |j|
      d = arr1[i] * arr2[j]
      res[i + j] += d % 10
      res[i + j + 1] += d / 10
    end
  end
  
  res.each_with_index do |v, i|
    next unless v > 9
    d = res[i]
    res[i] = d % 10
    res[i + 1] += d / 10
  end
  res.reverse.drop_while(&:zero?).join
end

num1 = '89948769547035'
num2 = '98'
p multiply(num1, num2)
