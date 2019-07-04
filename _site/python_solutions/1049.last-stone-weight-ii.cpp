/*
 * @lc app=leetcode id=1049 lang=cpp
 *
 * [1049] Last Stone Weight II
 *
 * https://leetcode.com/problems/last-stone-weight-ii/description/
 *
 * algorithms
 * Medium (38.32%)
 * Total Accepted:    3.5K
 * Total Submissions: 9.2K
 * Testcase Example:  '[2,7,4,1,8,1]'
 *
 * We have a collection of rocks, each rock has a positive integer weight.
 *
 * Each turn, we choose any two rocks and smash them together.  Suppose the
 * stones have weights x and y with x <= y.  The result of this smash is:
 *
 *
 * If x == y, both stones are totally destroyed;
 * If x != y, the stone of weight x is totally destroyed, and the stone of
 * weight y has new weight y-x.
 *
 *
 * At the end, there is at most 1 stone left.  Return the smallest possible
 * weight of this stone (the weight is 0 if there are no stones left.)
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [2,7,4,1,8,1]
 * Output: 1
 * Explanation:
 * We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
 * we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
 * we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
 * we can combine 1 and 1 to get 0 so the array converts to [1] then that's the
 * optimal value.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= stones.length <= 30
 * 1 <= stones[i] <= 100
 *
 */
using namespace std;
using VB = vector<bool>;
using VVB = vector<VB>;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)       // [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)
using VI = vector<int>;
int sum_(VI &a) { return accumulate(a.begin(), a.end(), 0); }

class Solution {
public:
  int lastStoneWeightII(vector<int> &stones) {
    int res = 0, mus = sum_(stones), s2 = mus / 2;
    VVB dp(s2 + 1, VB(stones.size() + 1, false));

    EACH(i, stones.size()) dp[0][i] = true;

    UP(s, 1, s2) UP(i, 1, stones.size()) {
      if (dp[s][i - 1] ||
          (s >= stones[i - 1] && dp[s - stones[i - 1]][i - 1])) {
        dp[s][i] = true;
        res = max(res, s);
      }
    }
    return mus - 2 * res;
  }
};
