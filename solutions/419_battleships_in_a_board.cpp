#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an 2D board, count how many battleships are in it. The battleships are
represented with 'X's, empty slots are represented with '.'s. You may assume the
following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they
can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
where N can be of any size.
At least one horizontal or vertical cell separates between two battleships -
there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always
have a cell separating between them.
Follow up:Could you do it in one-pass, using only O(1) extra memory and without
modifying the value of the board?
 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// The key point for this solution is: all boards are assumed to be valid. Thus
// we don't have to consider invalid cases.

class Solution {
public:
  int countBattleships(vector<vector<char>> &board) {
    if (0 == board.size())
      return 0;
    int res = 0;
    for (int i = 0; i < board.size(); i++)
      for (int j = 0; j < board[0].size(); j++) {
        if ('.' == board[i][j])
          continue;
        if (i > 0 && 'X' == board[i - 1][j])
          continue;
        if (j > 0 && 'X' == board[i][j - 1])
          continue;
        res++;
      }
    return res;
  }
};

int main() { Solution s; }
