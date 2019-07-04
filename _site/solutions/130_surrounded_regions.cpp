#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn&rsquo;t be on the border, which means that any 'O'on
the border of the board are not flipped to 'X'. Any 'O'that is not on the border
and it is not connected to an 'O'on the border will be flipped to 'X'. Two cells
are connected if they are adjacent cells connected horizontally or vertically.

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  void solve(vector<vector<char>> &board) {
    if (0 == board.size())
      return;
    int m = board.size(), n = board[0].size();
    vector<vector<int>> v(m, vector<int>(n, 0));

    for(int i=0; i < m; i ++) {
    	epidemic(board, v, i, 0);
    	epidemic(board, v, i, board[0].size() - 1);
    }

    for(int j=0; j < n; j ++){
    	epidemic(board, v, 0, j);
    	epidemic(board, v, board.size()-1, j);
	}

    for (int i = 0; i < m; i++)
    	for (int j = 0; j < n; j++)
    		if(v[i][j] < 1)
    			board[i][j] = 'X'; 

  }

  void epidemic(vector<vector<char>> &board, vector<vector<int>> &v, int i,
                int j) {
    if (i < 0 || j < 0 || i >= board.size() ||
        j >= board[0].size()) // not an item
      return;
    if (board[i][j] == 'X' ||
        v[i][j] == 1) // already be infected or is not an 'O'
      return;
    v[i][j] = 1;
    epidemic(board, v, i, j - 1);
    epidemic(board, v, i, j + 1);
    epidemic(board, v, i - 1, j);
    epidemic(board, v, i + 1, j);
  }
};

int main() {
  Solution s;
  vector<string> input = {"OXOOOX", "OOXXXO", "XXXXXO",
                          "OOOOXX", "XXOOXO", "OOXXXX"};
  vector<std::vector<char>> board;
  for (string sss : input) {
    vector<char> tmp;
    for (char c : sss)
      tmp.push_back(c);
    board.push_back(tmp);
  }

  s.solve(board);
  for (auto v : board) {
    for (char c : v)
      cout << c << " ";
    cout << endl;
  }
}
