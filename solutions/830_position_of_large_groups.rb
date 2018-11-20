# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.

# @param {String} s
# @return {Integer[][]}
def large_group_positions(s)
  r = []
  i = j = 0
  while j < s.size
    if s[i] != s[j]
      r << [i, j - 1] if j - i >= 3
      i = j
    end
    j += 1
  end
  r << [i, j - 1] if j - i >= 3
  r
end

s = 'abcdddeeeeaabbbcd'
s = 'abbxxxxzzy'
s = 'aaa'
p large_group_positions(s)
