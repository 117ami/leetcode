# coding: utf-8

=begin
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
=end

# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
  a, b = b, a if a.length < b.length
  a.reverse!
  b.reverse!
  r = []
  a.chars.each_with_index { |v, i| r[i] = v.to_i + b[i].to_i }
  r.each_with_index do |v, i|
    next if v < 2
    r[i] = v % 2
    r[i + 1] = r[i + 1].nil? ? v / 2 : r[i + 1] + v / 2
  end
  r.join.reverse
end

def add_binary_2(a, b)
  (a.to_i(2) + b.to_i(2)).to_s(2)
end

p add_binary('1110', '101')
