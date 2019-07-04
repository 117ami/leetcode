#
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
#
#  https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

# @param {String} s
# @param {String[]} d
# @return {String}
def find_longest_word(s, d)
  res = ''
  d.each do |str|
    if substring?(s, str)
      res = str.size > res.size ? str : str.size == res.size ? [res, str].min : res
    end
  end
  res
end

def substring?(s, str)
  return false if s.size < str.size
  i = j = 0
  while i < s.size && j < str.size
    if s[i] == str[j]
      i += 1
      j += 1
    else
      i += 1
    end
  end
  j == str.size
end

s = 'abpcplea'
d = %w[ale apple monkey plea]

# s = 'abpcplea'
# d = %w[a b c]
p find_longest_word(s, d)
