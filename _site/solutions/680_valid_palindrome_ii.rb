#  Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
#
# Input: "aba"
# Output: True
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
# Note:
#
#     The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
  i = 0
  i += 1 while i < s.length / 2 && s[i] == s[s.length - 1 - i]
  [[s.dup, i], [s.dup, s.length - 1 - i]].each do |t, j|
    t[j] = ''
    p [t, s]
    return true if t == t.reverse
  end
  false
end

def valid_palindrome2(s)
  left = -1
  right = s.length
  while left < right
    left += 1
    right -= 1
    next if s[left] == s[right]
    sa = s[left..right - 1]
    sb = s[left + 1..right]
    return sa == sa.reverse || sb == sb.reverse
  end
  true
end

s = 'aba'
s = 'abc'
p valid_palindrome(s)
p valid_palindrome2(s)
