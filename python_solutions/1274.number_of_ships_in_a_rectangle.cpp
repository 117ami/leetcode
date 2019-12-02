// https://leetcode.com/problems/number-of-ships-in-a-rectangle
// Hard (Difficulty)

// (This problem is an interactive problem.)
// On the sea represented by a cartesian plane, each ship is located at an
// integer point, and each integer point may contain at most 1 ship. You have a
// function Sea.hasShips(topRight, bottomLeft) which takes two points as
// arguments and returns true if and only if there is at least one ship in the
// rectangle represented by the two points, including on the boundary. Given two
// points, which are the top right and bottom left corners of a rectangle,
// return the number of ships present in that rectangle.  It is guaranteed that
// there are at most 10 ships in that rectangle. Submissions making more than
// 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that
// attempt to circumvent the judge will result in disqualification.   Example :
//
//  
// Constraints:
// Input:
// ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
// Output: 3
// Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
//
// xxxxxxxxxx
// /**
//  * // This is Sea's API interface.
//  * // You should not implement it, or speculate about its implementation
//  * class Sea {
//  *   public:
//  *     bool hasShips(vector<int> topRight, vector<int> bottomLeft);
//  * };
//  */
// ​
// class Solution {
// public:
//     int countShips(Sea sea, vector<int> topRight, vector<int> bottomLeft) {
//         
//     }
// };

class Solution {
public:
  int countShips(Sea sea, vector<int> q, vector<int> p) {
    if (!sea.hasShips(q, p))
      return 0;
    int x1 = p[0], y1 = p[1], x2 = q[0], y2 = q[1], ans = 0;

    if (x2 - x1 < 3 && y2 - y1 < 3) {
      for (int i = x1; i <= x2; i++) {
        for (int j = y1; j <= y2; j++) {
          vector<int> t = {i, j};
          ans += sea.hasShips(t, t) ? 1 : 0;
        }
      }
      return ans;
    } else {
      if (y2 - y1 > x2 - x1) {
        vector<int> m{x1, (y1 + y2) / 2 + 1}, n{x2, (y1 + y2) / 2};
      } else {
        vector<int> m{(x1 + x2) / 2 + 1, y1}, n{(x1 + x2) / 2, y2};
      }
      return countShips(sea, q, m) + countShips(sea, n, p);
    }
  }
};