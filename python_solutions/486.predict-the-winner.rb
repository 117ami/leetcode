#
# @lc app=leetcode id=486 lang=ruby
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (46.74%)
# Total Accepted:    48.5K
# Total Submissions: 103.8K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score.
#
# Example 1:
#
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2
# (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 +
# 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you
# need to return False.
#
#
#
# Example 2:
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose
# 233.Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
#
#
#
# Note:
#
# 1
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
#
#
#
# @param {Integer[]} nums
# @return {Boolean}
def predict_the_winner(nums)
  return true if nums.size <= 2
  pre = nums.dup
  cur = pre.dup

  1.upto(pre.size - 1).each do |len|
    0.upto(pre.size - 1 - len).each do |i|
      j = i + len
      cur[j] = [nums[i] - pre[j], nums[j] - pre[j - 1]].max
    end
    pre = cur.dup
  end
  p cur
  cur.last >= 0
end

# nums = [1, 5, 233, 7]
nums = [5, 3, 4, 5]
p predict_the_winner(nums)

# 100.times do |_|
# 	sz = Random.rand(30)
#   nums = sz.times.map { |_| Random.rand(1000) }
#   p predict_the_winner(nums) == old(nums)
# end
