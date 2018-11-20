
# Given a string s, find the longest palindromic substring in s. You may assume
#  that the maximum length of s is 1000.

def extend(a, i, j, maxlen)
  while i >= 0 && j < a.length && a[i] == a[j]
    i -= 1
    j += 1
  end

  maxlen = j - i - 2 if j - i - 2 > maxlen

  [maxlen, i + 1, j - 1]
end

# Question 5: longest palindromic substring
def lps(s)
  a = s.chars
  len = a.size
  return s if len < 2

  maxlen = 0
  low = 0
  high = 0

  (0..len - 1).each do |i|
    n, s, b = extend(a, i, i, maxlen)
    if n > maxlen
      low = s
      high = b
      maxlen = n
    end

    n, s, b = extend(a, i, i + 1, maxlen)
    next unless n > maxlen
    low = s
    high = b
    maxlen = n
  end
  a[low..high].join('')
end

s5 = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'

s5 = 'abcdedcfaaaafcd'
p lps(s5)
