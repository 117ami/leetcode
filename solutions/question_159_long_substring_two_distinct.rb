# Longest Substring with At Most Two (K) Distinct Characters
# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
#
# For example, Given s = “eceba”,
#
# T is "ece" which its length is 3.

def longest_substring(s, k)
  maxlen = 0
  start = ct = 0
  loc = {}
  s = s.chars

  s.each_with_index do |c, i|
    print "#{i}, #{c}, #{loc}, #{maxlen}\n"
    if loc.key?(c)
      loc[c] += 1
    else
      while ct == k
        loc[s[start]] -= 1
        if loc[s[start]].zero?
          loc.delete(s[start])
          ct -= 1
        end
        start += 1
      end
      loc[c] = 1
      ct += 1
    end
    maxlen = [maxlen, i - start + 1].max
  end

  maxlen
end

s = 'aababcbccbcba'
p longest_substring(s, 3)
