# require './aux.rb'
# @param {String[]} logs
# @return {String[]}
def reorder_log_files(logs)
  logs.map!(&:split)
  letters = logs.select { |s| s[1] =~ /[[:alpha:]]/ }.sort_by { |s| s[1..-1].join('*') + s.first }
  numbers = logs.select { |s| s[1] =~ /[[:digit:]]/ }
  (letters + numbers).map { |s| s.join(' ') }
end
# logs = ['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo', 'g0 act car']
logs = ['j mo', '5 m w', 'g 07', 'o 2 0', 't q h']
p reorder_log_files(logs)

# [937] Reorder Log Files
# https://leetcode.com/problems/reorder-log-files/description/
# * algorithms
# * Easy (55.73%)
# * Total Accepted:    4.6K
# * Total Submissions: 8.3K
# * Testcase Example:  '["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]'
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#   Each word after the identifier will consist only of lowercase letters, or;
#   Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
# Return the final order of the logs.
# Example 1:
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# Note:
#   0 <= logs.length <= 100
#   3 <= logs[i].length <= 100
#   logs[i] is guaranteed to have an identifier, and a word after the identifier.
