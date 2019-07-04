# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
# Example 1:
# Input: "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: "abcd"
# Output: "dcbabcd"
#

# @param {String} s
# @return {String}
def shortest_palindrome(s)
  xs = s + '*' + s.reverse
  pmt = Array.new(xs.size, -1)
  i = 0
  j = -1
  while i < xs.size
    if j == -1 || xs[i] == xs[j]
      i += 1
      j += 1
      pmt[i] = j
    else
      j = pmt[j]
    end
  end
  p pmt
  pmt[-1] == s.size ? s : s[pmt[-1]..s.size - 1].reverse + s
end

# to detect if there is a leading palindrome in s, return the length of the longest palindrome if there is one
def longest_palindrome(s)
  t = 0
  e = s.length - 1
  while e >= 0
    t += 1 if s[t] == s[e]
    e -= 1
  end
  #  t -= 1
  p s[0..t]
  compliment = s[t..-1].reverse
  compliment + shortest_palindrome(s[0...t]) + s[t..-1]
end

s = 'abcdpadacaebpa'
p shortest_palindrome(s)
p longest_palindrome(s)
