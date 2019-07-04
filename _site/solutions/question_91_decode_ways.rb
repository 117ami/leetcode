
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

# @param {String} s
# @return {Integer}
def num_decodings(s)
  cache = {}
  sub = lambda do |t|
    return 0 if t[0] == '0'
    return basic_cases(t) if t.length <= 2
    return cache[t] if cache.key?(t)
    cache[t] = if t[0..1].to_i > 26
                 sub.call(t[1..-1])
               elsif t[1] == '0' # 1, 0, ... or 2, 0, ...
                 sub.call(t[2..-1])
               else
                 sub.call(t[1..-1]) + sub.call(t[2..-1])
                 end
    return cache[t]
  end

  sub.call(s)
end

def basic_cases(s) # Size less than 3
  n = s.to_i
  return 0 if s.empty? || s[0] == '0' || n.zero? || n > 26 && (n % 10).zero?
  return 1 if n <= 10 || n == 20 || n > 26 && n % 10 > 0
  2
end

p num_decodings('01')
p num_decodings('9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253')
