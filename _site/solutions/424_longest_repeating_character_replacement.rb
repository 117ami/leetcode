# Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
# Note:
# Both the string's length and k will not exceed 104.
# Example 1:
# Input:
# s = "ABAB", k = 2
# Output:
# 4
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# Input:
# s = "AABABBA", k = 1
# Output:
# 4
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#

# @param {String} s
# @param {Integer} k
# @return {Integer}
def character_replacement(s, k)
  res =  start = 0
  counts = Hash.new(0)
  maxcount = 0
  s.each_char.with_index do |c, i|
    counts[c] += 1
    maxcount = [maxcount, counts[c]].max
    while i - start + 1 - maxcount > k
      counts[s[start]] -= 1
      start += 1
    end
    res = [res, i - start + 1].max
  end
  res
end

s = 'abcdefgab'
k = 2
p character_replacement(s, k)
