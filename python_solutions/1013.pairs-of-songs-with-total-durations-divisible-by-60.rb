#
# @lc app=leetcode id=1013 lang=ruby
#
# [1013] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (41.82%)
# Total Accepted:    4.5K
# Total Submissions: 10.8K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
# 
#
# @param {Integer[]} time
# @return {Integer}
def num_pairs_divisible_by60(time)
    c = time.map{|t| t % 60}.group_by(&:itself)
    ans = 0
    c.each_key do |k|
    	next if k > 30 
    	ans += c[k].size * (c[k].size - 1) / 2 if k.zero? || k == 30
    	next unless c.key?(60 - k)
    	ans += c[k].size * c[60 - k].size if k % 30 != 0
    end
    ans 
end

time = [30,20,150,100,40]
p num_pairs_divisible_by60(time)


