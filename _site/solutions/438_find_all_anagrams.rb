# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.

# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
  ph = Hash.new(0).tap { |h| p.each_char { |c| h[c] += 1 } }
  i = 0
  r = []
  cache = ph.dup
  (0..s.size - 1).each do |j|
    unless ph.key?(s[j])
      i = j + 1
      cache = ph.dup
      next
    end

    until cache.key?(s[j])
      cache[s[i]] += 1
      i += 1
    end

    cache[s[j]] -= 1
    cache.delete(s[j]) if cache[s[j]].zero?
    next unless cache.empty?
    r << i
    cache[s[i]] += 1
    i += 1
  end
  r
end

s = 'cbaebabacd'
# s = 'abab'
p = 'abc'
# p = 'ab'

s =

  p find_anagrams(s, p)
