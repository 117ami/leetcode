#include "aux.cpp"
/**
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is higher
or lower.
However, when you guess a particular number x,  and you guess wrong, you pay $x.
You win the game when you guess the number I picked.
Example:
n = 10, I pick 8.
First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.
Game over. 8 is the number I picked.
You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1, find out how much money you need to have to guarantee
a win.
Credits:Special thanks to @agave and @StefanPochmann for adding this problem and
creating all test cases.
 https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int getMoneyAmount(int n) {
    vector<vector<int>> v(n + 1, vector<int>(n + 1, 0));
    return dp(v, 1, n);
  }
  int dp(vector<vector<int>> &v, int i, int j) {
    if (i >= j)
      return 0;
    if (v[i][j] != 0)
      return v[i][j];
    int low = (i + j) / 2;
    v[i][j] = INT_MAX;
    for (int k = low; k <= j; k++)
      v[i][j] = min(v[i][j], k + max(dp(v, i, k - 1), dp(v, k + 1, j)));
    return v[i][j];
  }
};

int main() {
  Solution s;
  for (int i = 1; i < 11; i++)
    say(s.getMoneyAmount(i));
}
