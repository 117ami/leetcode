# require './aux.rb'
# @param {Integer} num
# @return {String[]}
def read_binary_watch(num)
  ans = []
  0.upto(num).each do |i|
    ans += poss_hours(i).product(poss_minutes(num - i)).map { |a| a.join(':') }
  end
  ans
end

def sum(arr) 
	arr.reduce(:+)
end

def poss_minutes(n)
  return ['00'] if n.zero?
  return [] if n > 5
  ans = [1, 2, 4, 8, 16, 32].combination(n).map(&:sum).select { |n| n < 60 }.map(&:to_s)
  ans.map { |s| s.length == 1 ? '0' + s : s }
end

def poss_hours(n)
  return [0] if n.zero?
  return [] if n > 3
  [1, 2, 4, 8].combination(n).map(&:sum).select { |n| n < 12 }
end

p read_binary_watch(2)
# [401] Binary Watch
# https://leetcode.com/problems/binary-watch/description/
# * algorithms
# * Easy (44.78%)
# * Total Accepted:    56K
# * Total Submissions: 125.1K
# * Testcase Example:  '0'
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs
# on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the right.
# For example, the above binary watch reads "3:25".
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
