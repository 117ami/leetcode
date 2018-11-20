
# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# Discuss

# @param {String} s
# @return {String}
# Method 1: use magic regexp
def decode_string(s)
  true while s.gsub!(/(\d+)\[([a-zA-Z]*)\]/) { Regexp.last_match(2) * Regexp.last_match(1).to_i }
  s
end

# Normal method with recursion
def rec_decode(s, i)
  res = ''
  while i < s.length && s[i] != ']'
    if s[i] =~ /[a-zA-Z]/
      res += s[i]
      i += 1
    else
      n = 0
      while i < s.length && s[i] =~ /\d/
        n = n * 10 + s[i].to_i
        i += 1
      end
      i += 1                    # '['
      i, t = rec_decode(s, i)
      i += 1                    # ']'
      res += t * n
    end
  end
  [i, res]
end

def decode_string_2(s)
  rec_decode(s, 0)[1]
end

r = decode_string_2('3[z]2[2[y]pq4[2[jk]e1[f]]]ef')
p r
p r == 'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
