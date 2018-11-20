# A string S of lowercase letters is given. Then, we may make any number of moves.
# In each move, wechoose oneof the first K letters (starting from the left), remove it,and place it at the end of the string.
# Return the lexicographically smallest string we could have after any number of moves.
#
# Example 1:
# Input: S = "cba", K = 1
# Output: "acb"
# Explanation:
# In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
# In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".
# Example 2:
# Input: S = "baaca", K = 3
# Output: "aaabc"
# Explanation:
# In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
# In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
#
# Note:
#   1 <= K <= S.length<= 1000
#   Sconsists of lowercase letters only.
#
#  https://leetcode.com/problems/orderly-queue/description/
require './aux.rb'

# @param {String} s
# @param {Integer} k
# @return {String}
def orderly_queue(s, k)
  return s.chars.sort.join if k > 1
  0.upto(s.size - 1).map { |i| s[i + 1..-1] + s[0..i] }.min
end

s = 10.times.map { Array('a'..'h').sample(1) }.flatten.join
k = 2
p s
p orderly_queue(s, k)
