
// #
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
// # Easy

class Solution {
public:
  bool is_win(vector<vector<char>> &gd, char c) {
    for (int i = 0; i < 3; i++) {
      if (gd[i][0] == c && gd[i][1] == c && gd[i][2] == c)
        return true;
      if (gd[0][i] == c && gd[1][i] == c && gd[2][i] == c)
        return true;
    }
    if (gd[0][0] == c && gd[1][1] == c && gd[2][2] == c)
      return true;
    if (gd[2][0] == c && gd[1][1] == c && gd[0][2] == c)
      return true;

    return false;
  }

  string tictactoe(vector<vector<int>> &ms) {
    if (ms.size() < 5)
      return "Pending";
    vector<vector<char>> gd(3, vector<char>(3, '#'));

    for (int i = 0; i < ms.size(); i++) {
      gd[ms[i][0]][ms[i][1]] = i & 1 ? 'O' : 'X';
    }

    char c = ms.size() & 1 ? 'X' : 'O';
    bool res = is_win(gd, c);
    if (res)
      return c == 'X' ? "A" : "B";
    else
      return ms.size() == 9 ? "Draw" : "Pending";
  }
};