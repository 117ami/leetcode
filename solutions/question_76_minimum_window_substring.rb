
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
  return '' if s.empty? || t.empty?
  need = Hash.new(0).tap { |h| t.each_char { |c| h[c] += 1 } }
  missing = t.length
  start = left = 0
  len = 2**32
  # Notice here we change s into an array. Because we later frequently take values from s
  #  str[i] is way slower than arr[i]. 
  s = s.chars                   

  s.each_with_index do |c, i|
    if need.key?(c)
      missing -= 1 if need[c] > 0
      need[c] -= 1
    end

    while missing.zero?
      if i - left <= len
        len = i - left
        start = left
      end

      if need.key?(s[left])
        need[s[left]] += 1
        missing += 1 if need[s[left]] > 0
      end
      left += 1
    end
  end
  
  return "" if len == 2*32
  print "#{start}, #{len}, #{s[start..start + len]}\n"
  s[start..start + len].join
end

s = 'ADOBECODEBANCD'
t = 'ABC'
#s = 'ab'
#t = 'a'
p min_window(s, t)
