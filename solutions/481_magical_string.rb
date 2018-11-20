#
# A magical string S consists of only '1' and '2' and obeys the following rules:
# The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.
# The first few elements of string S is the following:
# S = "1221121221221121122……"
# If we group the consecutive '1's and '2's in S, it will be:
# 1   22  11  2  1  22  1  22  11  2  11  22 ......
# and the occurrences of '1's or '2's in each group are:
# 1   2     2    1   1    2     1    2     2    1    2    2 ......
# You can see that the occurrence sequence above is the S itself.
# Given an integer N as input, return the number of '1's in the first N number in the magical string S.
# Note:
# N will not exceed 100,000.
# Example 1:
# Input: 6
# Output: 3
# Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
#
#  https://leetcode.com/problems/magical-string/description/
require './aux.rb'

# @param {Integer} n
# @return {Integer}
def magical_string(n)
	return 0 if n.zero?
  sc = %w[1 2 2]
  idx = 2
  sz = 3
  while sz < n
    if sc[idx] == '1'
      item = sc.last == '1' ? '2' : '1'
      sc << item
      sz += 1
    else
      item = sc.last == '1' ? '2' : '1'
      sc << item
      sc << item
      sz += 2
    end
    idx += 1
  end
  sc[0..n - 1].count('1')
end

s = '1221121221221121122'
freq = s.chars.map(&:to_i)

[10, 100, 1000, 10000, 100000].each do |n|
  p [n, magical_string(n)]
end
