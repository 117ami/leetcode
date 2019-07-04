#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
   Given n points in the plane that are all pairwise distinct, a "boomerang" is
a tuple of points (i, j, k) such that the distance between i and j equals the
distance between i and k (the order of the tuple matters).
   Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).
   Example:
   Input:
   [[0,0],[1,0],[2,0]]
   Output:
   2
   Explanation:
   The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int numberOfBoomerangs(vector<pair<int, int>> &points) {
    int res = 0;
    for (int i = 0; i < points.size(); i++) {
      int tmp[points.size()] = {0};
      for (int j = 0; j < points.size(); j++) 
        if (i != j)
	  tmp[j] = distance(points[i], points[j]);

      sort(tmp, tmp + points.size());
      int cter = 1;
      for (int i = 1; i < points.size(); i++)
        if (tmp[i] == tmp[i - 1])
          cter += 1;
        else {
          res += (cter - 1) * cter;
          cter = 1;
        }
      if (cter > 1)
        res += (cter - 1) * cter;
    }
    return res;
  }

  int distance(pair<int, int> pa, pair<int, int> pb) {
    return pow(pa.first - pb.first, 2) + pow(pa.second - pb.second, 2);
  }
};

int main() {
  Solution s;
  pair<int, int> pa{0, 0};
  pair<int, int> pb{1, 0};
  pair<int, int> pc{-1, 0};
  pair<int, int> pd{0, 1};
  pair<int, int> pe{0, -1};
  //  cout << s.distance(pa, pb) << endl;
  vector<pair<int, int>> points = {pa, pb, pc, pd, pe};
  cout << s.numberOfBoomerangs(points) << endl;
}
