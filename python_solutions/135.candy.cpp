/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 *
 * https://leetcode.com/problems/candy/description/
 *
 * algorithms
 * Hard (31.59%)
 * Total Accepted:    133.3K
 * Total Submissions: 421.8K
 * Testcase Example:  '[1,0,2]'
 *
 * There are N children standing in a line. Each child is assigned a rating
 * value.
 *
 * You are giving candies to these children subjected to the following
 * requirements:
 *
 *
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.
 *
 *
 * What is the minimum candies you must give?
 *
 * Example 1:
 *
 *
 * Input: [1,0,2]
 * Output: 5
 * Explanation: You can allocate to the first, second and third child with 2,
 * 1, 2 candies respectively.
 *
 *
 * Example 2:
 *
 *
 * Input: [1,2,2]
 * Output: 4
 * Explanation: You can allocate to the first, second and third child with 1,
 * 2, 1 candies respectively.
 * ⁠            The third child gets 1 candy because it satisfies the above
 * two conditions.
 *
 *
 */
class Solution {
public:
  int candy(vector<int> &ratings) {
    ios_base::sync_with_stdio(false);
    
    size_t n = ratings.size();
    vector<int> res(n, 1);

    for (size_t i = 1; i < n; i++)
      if (ratings[i] > ratings[i - 1])
        res[i] = res[i - 1] + 1;

    for (int i = n - 2; i >= 0; i--)
      if (ratings[i] > ratings[i + 1])
        res[i] = max(res[i + 1] + 1, res[i]);

    // say(res);
    return std::accumulate(res.begin(), res.end(), 0);
  }
};
