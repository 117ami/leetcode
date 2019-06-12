/*
 * @lc app=leetcode id=264 lang=cpp
 *
 * [264] Ugly Number II
 *
 * https://leetcode.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (36.45%)
 * Total Accepted:    105.3K
 * Total Submissions: 288.7K
 * Testcase Example:  '10'
 *
 * Write a program to find the n-th ugly number.
 *
 * Ugly numbers are positive numbers whose prime factors only include 2, 3,
 * 5. 
 *
 * Example:
 *
 *
 * Input: n = 10
 * Output: 12
 * Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
 * ugly numbers.
 *
 * Note:  
 *
 *
 * 1 is typically treated as an ugly number.
 * n does not exceed 1690.
 *
 */
using namespace std;
using vi = vector<int>;
using ll = long long;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)       // [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)
int vec_min(vi &a) { return *min_element(a.begin(), a.end()); }
#define fori(n) for (int i = 0; i <= int(n); ++i) // [0, n)

class Solution {
public:
  int nthUglyNumber(int n) {
    vi res(n, 1);
    vi exp(3, 0), ps = {2, 3, 5};
    UP(i, 1, n - 1) {
      res[i] = min(2*res[exp[0]], min(3*res[exp[1]], 5*res[exp[2]]));
      EACH(j, 2) if (res[i] == res[exp[j]] * ps[j]) exp[j] += 1;
    }
    // say(res);
    return res.back();
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
