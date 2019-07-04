using VI = vector<int>;
int sum_(VI &a) { return accumulate(a.begin(), a.end(), 0); }
#define DWN_1(i, b, a) for (int i = int(b); i >= a; --i)        // reverse [a, b]


class Solution {
public:
  int findTargetSumWays(vector<int> &nums, int S) {
    int sum = sum_(nums);
    if (S > sum || (sum + S) & 1)
      return 0;

    int s2 = (S + sum) >> 1;
    VI dp(sum + 1, 0);
    dp[0] = 1;
    for (auto &n : nums)
      DWN_1(i, s2, n) { dp[i] += dp[i - n]; }
    // say(dp);
    return dp[s2];
  }
};
