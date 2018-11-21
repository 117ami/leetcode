require './aux.rb'
# @param {String[]} a
# @return {Integer}
def min_deletion_size(a)
  a.map!(&:chars).transpose.count { |row| row.sort != row }
end
a = %w[cbad dafd ghic]
p min_deletion_size(a)
# [944] Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
# * algorithms
# * Medium (73.34%)
# * Total Accepted:    3.3K
# * Total Submissions: 4.5K
# * Testcase Example:  '["cba","daf","ghi"]'
# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have a string "abcdef" and deletion indices {0, 2, 3}, then the final string after deletion is "bef".
# Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
# Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]
# Return the minimum possible value of D.length.
# Example 1:
# Input: ["cba","daf","ghi"]
# Output: 1
# Example 2:
# Input: ["a","b"]
# Output: 0
# Example 3:
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Note:
#   1 <= A.length <= 100
#   1 <= A[i].length <= 1000
