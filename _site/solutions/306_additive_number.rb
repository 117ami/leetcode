# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
#              1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199.
#              1 + 99 = 100, 99 + 100 = 199

# @param {String} s
# @return {Integer[]}
def Fibonacci?(sa, sb, s)
  a = sa.to_i
  b = sb.to_i
  seqs = [sa, sb]
  loop do
    n = a + b
    # return [false, []] if n > 2 ** 31 - 1 || n < 0
    sn = n.to_s
    seqs << sn
    return false if sn.length > s.length || sn != s[0..sn.length - 1]
    s[0..sn.length - 1] = ''
    p seqs if s == ''
    return true if s == ''
    a = b
    b = n
  end
end

def is_additive_number(s)
  r = s.scan(/^(0*)/)
  return false if s.length < 3 ||
                  s.length == 3 && s[0].to_i + s[1].to_i != s[2].to_i
  return true if r[0][0].length == s.length
  return false if r[0][0].length > 1

  ibound = r[0][0].length == 1 ? 0 : s.length / 2 - 1

  (0..ibound).each do |i|
    (i + 1..s.length - 1).each do |j|
      break if s[i + 1] == '0' && j > i + 1
      break if [i + 1, j - i].max > s.length - j - 1
      r = Fibonacci?(s[0..i], s[i + 1..j], s[j + 1..s.length - 1])
      return true if r
    end
  end
  false
end

s = '1123582'
s = '000'
s = '199001200'
p is_additive_number(s)
