# Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
#
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
#
#     0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
#     F.length >= 3;
#     and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
#
# Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
#
# Example 1:
#
# Input: "123456579"
# Output: [123,456,579]
#
# Example 2:
#
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
#
# Example 3:
#
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
#
# Example 4:
#
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
#
# Example 5:
#
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
#
# Note:
#
#     1 <= S.length <= 200
#     S contains only digits.

# @param {String} s
# @return {Integer[]}
def Fibonacci?(sa, sb, s)
  a = sa.to_i
  b = sb.to_i
  seqs = [sa, sb]
  loop do
    n = a + b
    return [false, []] if n > 2 ** 31 - 1 || n < 0
    sn = n.to_s
    seqs << sn
    return [false, []] if sn.length > s.length || sn != s[0..sn.length - 1]
    s[0..sn.length - 1] = ''
    return [true, seqs] if s == ''
    a = b
    b = n
  end
end

def split_into_fibonacci(s)
  r = s.scan(/^(0*)/)
  return [] if s.length < 3 ||
               s.length == 3 && s[0].to_i + s[1].to_i != s[2].to_i

  return Array.new(s.length, 0) if r[0][0].length == s.length
  return [] if r[0][0].length > 1
  ibound = r[0][0].length == 1 ? 0 : s.length / 2 - 1

  (0..ibound).each do |i|
    (i + 1..s.length - 1).each do |j|
      break if [i + 1, j - i].max > s.length - j - 1
      r = Fibonacci?(s[0..i], s[i + 1..j], s[j + 1..s.length - 1])
      return r[1].map(&:to_i) if r[0]
    end
  end
  []
end

s = '1101111'
s = '0000'
s = '539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511'
# expected []
p split_into_fibonacci(s)
