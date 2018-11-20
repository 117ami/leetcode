#include "aux.cpp"
/**
Given two integer arrays A and B, return the maximum length of an subarray that
appears in both arrays. Example 1: Input: A: [1,2,3,2,1] B: [3,2,1,4,7] Output:
3 Explanation: The repeated subarray with maximum length is [3, 2, 1]. Note: 1
<= len(A), len(B) <= 1000 0 <= A[i], B[i] < 100

 https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int findLength(vector<int> &a, vector<int> &b) {
    vector<vector<int>> dp(a.size() + 1, vector<int>(b.size() + 1));
    int res = 0;
    for (int i = 0; i <= a.size(); i++)
      for (int j = 0; j <= b.size(); j++)
        if (i == 0 || j == 0)
          dp[i][j] = 0;
        else if (a[i - 1] == b[j - 1]) {
          dp[i][j] = 1 + dp[i - 1][j - 1];
          res = max(dp[i][j], res);
        }
    // say(dp);
    return res;
  }
};

int main() {
  Solution s;
  vector<int> a = {1, 2, 3, 2, 1};
  vector<int> b = {3, 2, 2};
  say(s.findLength(a, b));
}
