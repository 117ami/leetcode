#  Given two strings representing two complex numbers.
#
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#
# Example 1:
#
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
#
# Example 2:
#
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
#
# Note:
#
#     The input strings will not have extra blank.
#     The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

def number2array(n) # return an array represents a complex number
  x = n.split('')
end

# @param {String} a
# @param {String} b
# @return {String}
def complex_number_multiply(a, b)
  re = im = 0
  x = a.match(/^(-?\d+)(\+|\-)(.*)(i)/)[1..-1]
  y = b.match(/^(-?\d+)(\+|\-)(.*)(i)/)[1..-1]
  
  re = if x[1] == y[1]
         x[0].to_i * y[0].to_i - x[2].to_i * y[2].to_i
       else
         x[0].to_i * y[0].to_i + x[2].to_i * y[2].to_i
       end

  im += y[1] == '+' ? x[0].to_i * y[2].to_i : x[0].to_i * y[2].to_i * -1
  im += x[1] == '+' ? y[0].to_i * x[2].to_i : y[0].to_i * x[2].to_i * -1
  
  [re, '+', im, 'i'].join
end

a = '78+-76i'
b = '-86+72i'
p complex_number_multiply(a, b)
