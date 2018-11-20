# require './aux.rb'
# @param {String} s
# @return {Integer[]}
def di_string_match(s)
  arr = 0.upto(s.length).to_a
  ans = []
  s.each_char do |c|
    ans << if c == 'I'
             arr.shift
           else
             arr.pop
           end
  end
  ans << arr.pop
  ans
end

# [942] DI String Match
# https://leetcode.com/problems/di-string-match/description/
# * algorithms
# * Easy (65.79%)
# * Total Accepted:    3.7K
# * Total Submissions: 5.7K
# * Test case Example:  '"IDID"'
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#   If S[i] == "I", then A[i] < A[i+1]
#   If S[i] == "D", then A[i] > A[i+1]
# Example 1:
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
# Input: "DDI"
# Output: [3,2,0,1]
# Note:
#   1 <= S.length <= 10000
#   S only contains characters "I" or "D".
