# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
# Output: "012"
# Example 2:
# Input: "fviefuro"
# Output: "45"
#
# @param {String} s
# @return {String}
def original_digits(s)
  letters = Hash.new(0)
  s.each_char { |c| letters[c] += 1 }
  res = []
  decode = lambda do |c, n, word|
    while letters[c] > 0
      res << n
      word.each_char { |w| letters[w] -= 1 }
    end
  end
  decode.call('z', 0, 'zero')
  decode.call('w', 2, 'two')
  decode.call('x', 6, 'six')
  decode.call('u', 4, 'four')
  decode.call('g', 8, 'eight')
  decode.call('h', 3, 'three')
  decode.call('f', 5, 'five')
  decode.call('s', 7, 'seven')
  decode.call('o', 1, 'one')
  decode.call('i', 9, 'nine')
  res.sort.join
end

s = 'twoneo'
s = 'onthrzerosevoneeneeetzerfoureightsixeightnineowo'
p original_digits(s)
