#include "aux.cpp"
/**

An integer interval [a, b] (for integers a < b) is a set of all consecutive
integers from a to b, including a and b.
Find the minimum size of a set S such that for every integer interval A in
intervals, the intersection of S with A has size at least 2.
Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2
elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
Note:
intervals will have length in range [1, 3000].
intervals[i] will have length 2, representing some integer interval.
intervals[i][j] will be an integer in [0, 10^8].

 https://leetcode.com/problems/set-intersection-size-at-least-two/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int intersectionSizeTwo(vector<vector<int>> &intervals) {
    sort(intervals.begin(), intervals.end(),
         [](const vector<int> &a, const vector<int> &b) {
           return a[1] < b[1] || a[1] == b[1] && a[0] > b[0];
         });
    int res = 0, pa = -1, pb = -1;
    for (auto iv : intervals) {
      if (iv[0] <= pa)
        continue;
      if (iv[0] > pb) {
        res += 2;
        pb = iv[1];
        pa = pb - 1;
      } else {
        res += 1;
        pa = pb;
        pb = iv[1];
      }
    }
    return res;
  }
};
int main() { Solution s; }
