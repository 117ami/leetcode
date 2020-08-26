#include <vector>
#include <iostream>
using namespace std;

vector<vector<int>> pre_sum(vector<vector<int>> &mat) {
  /* presum of 2D array ;
   */
  int m = mat.size(), n = mat[0].size();
  vector<vector<int>> ans(m, vector<int>(n, 0));
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (i == 0 && j == 0)
        ans[i][j] = mat[i][j];
      else if (i == 0 && j > 0) {
        ans[i][j] = ans[i][j - 1] + mat[i][j];
      } else if (i > 0 && j == 0) {
        ans[i][j] = ans[i - 1][j] + mat[i][j];
      } else {
        ans[i][j] =
            ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1] + mat[i][j];
      }
    }
  }
  return ans;
}

vector<int> pre_sum(vector<int> &ns) {
  int n = ns.size();
  vector<int> res(ns.begin(), ns.end());
  for (int i = 1; i < n; i++)
    res[i] += res[i - 1];
  return res;
}

int main() {
    using namespace std;
  vector<int> x = {1, 2, 3};
  vector<int> y = pre_sum(x);
  for (auto i : y)
    cout << i << endl;
  return 0;
}
