#     There are N children standing in a line. Each child is assigned a rating value.
#     You are giving candies to these children subjected to the following requirements:
#       Each child must have at least one candy.
#       Children with a higher rating get more candies than their neighbors.
#     What is the minimum candies you must give?
#     Example 1:
#     Input: [1,0,2]
#     Output: 5
#     Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#     Example 2:
#     Input: [1,2,2]
#     Output: 4
#     Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#                  The third child gets 1 candy because it satisfies the above two conditions.
#
#      https://leetcode.com/problems/candy/description/

require './aux.rb'

# @param {Integer[]} ratings
# @return {Integer}
def candy(ratings)
  return ratings.size if ratings.size < 2
  res = [1] * ratings.size
  1.upto(res.size - 1) { |i| res[i] = [res[i], res[i - 1] + 1].max if ratings[i] > ratings[i - 1] }
  (res.size - 2).downto(0) { |i| res[i] = [res[i], res[i + 1] + 1].max if ratings[i] > ratings[i + 1] }
  res.reduce(:+)
end

ratings = random_list(9, 10)
# ratings = [9, 7, 9, 5, 1, 3, 6, 6, 7]
ratings = [1, 3, 4, 5, 2]
p ratings
p candy(ratings)
