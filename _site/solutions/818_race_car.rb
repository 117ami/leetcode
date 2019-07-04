# Your car starts at position 0 and speed +1 on an infinite number line. (Your car can go into negative positions.)
# Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
# When you get an instruction "A", your car does the following:position += speed, speed *= 2.
# When you get an instruction "R", your car does the following: if your speed is positive thenspeed = -1, otherwisespeed = 1. (Your position stays the same.)
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
# Now for some target position, say the length of the shortest sequence of instructions to get there.
# Example 1:
# Input:
# target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# Example 2:
# Input:
# target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#
# Note:
#   1 <= target <= 10000.
#
#  https://leetcode.com/problems/race-car/description/
require './aux.rb'

# @param {Integer} target
# @return {Integer}

def racecar(target)
  dp = Array.new(10_001, Float::INFINITY)
  dp[1] = 1
  dp[3] = 2
  helper = lambda do |t|
    return dp[t] if dp[t] < Float::INFINITY
    n = Math.log2(t).floor + 1
    return n if 1 + t == 1 << n
    dp[t] = helper.call((1 << n) - t - 1) + n + 1
    (0..n - 2).each do |m| # here the upper bound is n-2 instead of n-1 because 1 << (n-1) + 1 << (n-1) = 1 << n > target 
      dp[t] = [dp[t], helper.call(t - (1 << (n - 1)) + (1 << m)) + m + n + 1].min
    end
    dp[t]
  end
  helper.call(target)
end

target = 9
p racecar(target)
