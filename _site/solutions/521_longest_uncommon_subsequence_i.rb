#  Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
#
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

# @param {String} a
# @param {String} b
# @return {Integer}
def find_lu_slength(a, b)
  a == b ? -1 : [a.length, b.length].max
end

a = 'aefawfawfawfaw'
b = 'aefawfeawfwafwaef'

p find_lu_slength(a, b)
