# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
  return false unless s.length == t.length
  s.split('').sort == t.split('').sort
end

def is_anagram2(s, t)
  has = Hash.new(0).tap { |h| s.each_char { |c| h[c] += 1 } }
  t.each_char do |c|
    return false unless has.key?(c)
    has[c] -= 1
    has.delete(c) if has[c].zero?
  end
  has.empty?
end

def is_anagram3(s, t)
  return false unless s.length == t.length
  count = Hash.new(0)
  (0..s.length - 1).each do |i|
    count[s[i]] += 1
    count[t[i]] -= 1
  end
  count.each_value { |v| return false unless v.zero? }
  true
end

s = 'anagram'
t = 'nagaram'
p is_anagram(s, t)
p is_anagram2(s, t)
p is_anagram3(s, t)
