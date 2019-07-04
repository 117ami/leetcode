/*
 * @lc app=leetcode id=949 lang=cpp
 *
 * [949] Largest Time for Given Digits
 *
 * https://leetcode.com/problems/largest-time-for-given-digits/description/
 *
 * algorithms
 * Easy (34.00%)
 * Total Accepted:    8.7K
 * Total Submissions: 25.6K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array of 4 digits, return the largest 24 hour time that can be
 * made.
 *
 * The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
 * 00:00, a time is larger if more time has elapsed since midnight.
 *
 * Return the answer as a string of length 5.  If no valid time can be made,
 * return an empty string.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,2,3,4]
 * Output: "23:41"
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [5,5,5,5]
 * Output: ""
 *
 *
 *
 *
 * Note:
 *
 *
 * A.length == 4
 * 0 <= A[i] <= 9
 *
 *
 *
 */
using namespace std;
using vi = vector<int>;
using ll = long long;
using namespace std;
#include <cassert>
#define mp make_pair
#define ALL(v) v.begin(), v.end()
inline string itos(int n) { return to_string(n); }

class Solution {
public:
  string largestTimeFromDigits(vector<int> &v) {
    sort(ALL(v), greater<int>());
    do {
      if (valid(v))
        return itos(v[0]) + itos(v[1]) + ":" + itos(v[2]) + itos(v[3]);
    } while (prev_permutation(v.begin(), v.end()));
    return "";
  }

  bool valid(vi &a) {
    return (a[0] * 10 + a[1]) < 24 && (a[2] * 10 + a[3] < 60);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
