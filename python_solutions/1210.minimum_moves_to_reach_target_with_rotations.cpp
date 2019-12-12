// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations
// Hard (Difficulty)

// In an n*n grid, there is a snake that spans 2 cells and starts moving from
// the top left corner at (0, 0) and (0, 1). The grid has empty cells
// represented by zeros and blocked cells represented by ones. The snake wants
// to reach the lower right corner at (n-1, n-2) and (n-1, n-1). In one move the
// snake can: Return the minimum number of moves to reach the target. If there
// is no way to reach the target, return -1.   Example 1:
//
// Example 2:
//  
// Constraints:
// Input: grid = [[0,0,0,0,0,1],
//                [1,1,0,0,1,0],
//                [0,0,0,0,1,1],
//                [0,0,1,0,1,0],
//                [0,1,1,0,0,0],
//                [0,1,1,0,0,0]]
// Output: 11
// Explanation:
// One possible solution is [right, right, rotate clockwise, right, down, down,
// down, down, rotate counterclockwise, right, down].
//
// Input: grid = [[0,0,1,1,1,1],
//                [0,0,0,0,1,1],
//                [1,1,0,0,0,1],
//                [1,1,1,0,0,1],
//                [1,1,1,0,0,1],
//                [1,1,1,0,0,0]]
// Output: 9
//
// xxxxxxxxxx
// class Solution {
// public:
//     int minimumMoves(vector<vector<int>>& grid) {
//         
//     }
// };
class Solution {
private:
  struct snakepos {
    int x, y, state, len;
  };

public:
  int minimumMoves(vector<vector<int>> &grid) {
    int n = grid.size(), res = -1;
    int visited[n][n][2];
    memset(visited, 0, sizeof(visited));
    queue<snakepos> q;
    visited[0][0][0] = 1;
    q.push(snakepos{0, 0, 0, 0});
    while (!q.empty()) {
      snakepos now = q.front();
      q.pop();
      if (now.x == n - 1 && now.y == n - 2 && now.state == 0) {
        res = now.len;
        break;
      } else if (now.state == 0) {
        if (now.y + 2 < n && grid[now.x][now.y + 2] == 0 &&
            !visited[now.x][now.y + 1][0]) {
          visited[now.x][now.y + 1][0] = 1;
          q.push(snakepos{now.x, now.y + 1, 0, now.len + 1});
        }
        if (now.x + 1 < n && grid[now.x + 1][now.y] == 0 &&
            grid[now.x + 1][now.y + 1] == 0) {
          if (!visited[now.x + 1][now.y][0]) {
            visited[now.x + 1][now.y][0] = 1;
            q.push(snakepos{now.x + 1, now.y, 0, now.len + 1});
          }
          if (!visited[now.x][now.y][1]) {
            visited[now.x][now.y][1] = 1;
            q.push(snakepos{now.x, now.y, 1, now.len + 1});
          }
        }
      } else {
        if (now.x + 2 < n && grid[now.x + 2][now.y] == 0 &&
            !visited[now.x + 1][now.y][1]) {
          visited[now.x + 1][now.y][1] = 1;
          q.push(snakepos{now.x + 1, now.y, 1, now.len + 1});
        }
        if (now.y + 1 < n && grid[now.x][now.y + 1] == 0 &&
            grid[now.x + 1][now.y + 1] == 0) {
          if (!visited[now.x][now.y + 1][1]) {
            visited[now.x][now.y + 1][1] = 1;
            q.push(snakepos{now.x, now.y + 1, 1, now.len + 1});
          }
          if (!visited[now.x][now.y][0]) {
            visited[now.x][now.y][0] = 1;
            q.push(snakepos{now.x, now.y, 0, now.len + 1});
          }
        }
      }
    }
    return res;
  }
};