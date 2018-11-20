#include "aux.cpp"
/**
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following
requirements: Each child must have at least one candy. Children with a higher
rating get more candies than their neighbors. What is the minimum candies you
must give? Example 1: Input: [1,0,2] Output: 5 Explanation: You can allocate to
the first, second and third child with 2, 1, 2 candies respectively. Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1
candies respectively. The third child gets 1 candy because it satisfies the
above two conditions.

 https://leetcode.com/problems/candy/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int candy(vector<int> &ratings) {
    vector<int> res(ratings.size(), 1);
    for (int i = 1; i < ratings.size(); i++)
      if (ratings[i] > ratings[i - 1])
        res[i] = max(res[i], res[i - 1] + 1);

    for (int i = ratings.size() - 2; i >= 0; i--)
      if (ratings[i] > ratings[i + 1])
        res[i] = max(res[i], res[i + 1] + 1);

    say(res);
    return accumulate(res.begin(), res.end(), 0);
  }
};

int main() {
  Solution s;
  vector<int> ratings = randvector(20, 10);
  say(ratings);
  say(s.candy(ratings));
}
