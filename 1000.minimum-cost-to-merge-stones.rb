#
# @lc app=leetcode id=1000 lang=ruby
#
# [1000] Minimum Cost to Merge Stones
#
# https://leetcode.com/problems/minimum-cost-to-merge-stones/description/
#
# algorithms
# Hard (29.69%)
# Total Accepted:    3K
# Total Submissions: 10.1K
# Testcase Example:  '[3,2,4,1]\n2'
#
# There are N piles of stones arranged in a row.  The i-th pile has stones[i]
# stones.
#
# A move consists of merging exactly K consecutive piles into one pile, and the
# cost of this move is equal to the total number of stones in these K piles.
#
# Find the minimum cost to merge all piles of stones into one pile.  If it is
# impossible, return -1.
#
#
#
#
# Example 1:
#
#
# Input: stones = [3,2,4,1], K = 2
# Output: 20
# Explanation:
# We start with [3, 2, 4, 1].
# We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
# We merge [4, 1] for a cost of 5, and we are left with [5, 5].
# We merge [5, 5] for a cost of 10, and we are left with [10].
# The total cost was 20, and this is the minimum possible.
#
#
#
# Example 2:
#
#
# Input: stones = [3,2,4,1], K = 3
# Output: -1
# Explanation: After any merge operation, there are 2 piles left, and we can't
# merge anymore.  So the task is impossible.
#
#
#
# Example 3:
#
#
# Input: stones = [3,5,1,2,6], K = 3
# Output: 25
# Explanation:
# We start with [3, 5, 1, 2, 6].
# We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
# We merge [3, 8, 6] for a cost of 17, and we are left with [17].
# The total cost was 25, and this is the minimum possible.
#
#
#
#
# Note:
#
#
# 1 <= stones.length <= 30
# 2 <= K <= 30
# 1 <= stones[i] <= 100
#
#
#
#
#
# @param {Integer[]} stones
# @param {Integer} k
# @return {Integer}
def merge_stones(stones, k)
  return -1 if (stones.size - 1) % (k - 1) != 0
  dp = Array.new(stones.size){|_| Array.new(stones.size, Float::INFINITY)}
  len = k 
  while len <= stones.size 
  # k.upto(stones.size).each do |len|
  	1.upto(stones.size-len + 1).each do |i|
  		j = i + len - 1  		
      
  		if len == k  
  			dp[i][j] = number[i..j].reduce(:+)
  		else
		  	dp[i][j] = [dp[i][j], ].min  			
  		end
  	end
  end
end



