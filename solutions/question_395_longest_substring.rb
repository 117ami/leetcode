
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_substring(s, k)
  return 0 if k > s.length
  min_chars = s.chars.keep_if { |c| s.count(c) < k }
  return s.length if min_chars.empty?

  min_chars.each { |c| s.tr!(c, ',') }
  r = 0
  s.split(/,/).each do |subs|
    r = [r, longest_substring(subs, k)].max
  end
  r
end

# faster than above
def longest_substring_2(s, k)
  return 0 if k > s.length
  r = 0
  occur = {}
  s.each_char do |c|
    occur.key?(c) ? occur[c] += 1 : occur[c] = 1
  end

  chars = occur.keys.keep_if { |c| occur[c] < k }
  return s.length if chars.empty?
  chars.map { |c| s.tr!(c, ',') }

  s.split(/,/).each do |subs|
    r = [r, longest_substring(subs, k)].max
  end
  r
end

p longest_substring('ababbceaklfdasalkdjflaj', 2)
