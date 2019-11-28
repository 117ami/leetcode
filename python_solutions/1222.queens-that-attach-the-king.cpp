// 
//  @lc app=leetcode id=1222 lang=python3
// 
//  [1222] queens that attach the king
// 
//  algorithms
//  Medium (50.43%)
//  https://leetcode.com/problems/queens-that-can-attack-the-king/


class Solution {
public:
  vector<vector<int>> queensAttacktheKing(vector<vector<int>> &queens,
                                          vector<int> &king) {
    unordered_set<int> seen;
    for (auto &q : queens)
      seen.insert(q[0] * 10 + q[1]);

    vector<vector<int>> res;

    int directions[8][2] = {{-1, 0},  {1, 0},  {0, -1}, {0, 1},
                            {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
    for (auto &d : directions) {
      int i = king[0], j = king[1];
      while (i >= 0 && j >= 0 && i < 8 && j < 8 &&
             seen.find(i * 10 + j) == seen.end()) {
        i += d[0], j += d[1];
      }
      if (i >= 0 && j >= 0 && i < 8 && j < 8)
        res.push_back(vector<int>{i, j});
    }

    return res;
  }
};