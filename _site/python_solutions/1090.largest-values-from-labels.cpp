/*
 * @lc app=leetcode id=1090 lang=cpp
 *
 * [1090] Largest Values From Labels
 *
 * https://leetcode.com/problems/largest-values-from-labels/description/
 *
 * algorithms
 * Medium (53.75%)
 * Total Accepted:    2.6K
 * Total Submissions: 4.8K
 * Testcase Example:  '[5,4,3,2,1]\n[1,1,2,2,3]\n3\n1'
 *
 * We have a set of items: the i-th item has value values[i] and label
 * labels[i].
 *
 * Then, we choose a subset S of these items, such that:
 *
 *
 * |S| <= num_wanted
 * For every label L, the number of items in S with label L is <= use_limit.
 *
 *
 * Return the largest possible sum of the subset S.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit
 * = 1
 * Output: 9
 * Explanation: The subset chosen is the first, third, and fifth item.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit
 * = 2
 * Output: 12
 * Explanation: The subset chosen is the first, second, and third item.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
 * = 1
 * Output: 16
 * Explanation: The subset chosen is the first and fourth item.
 *
 *
 *
 * Example 4:
 *
 *
 * Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
 * = 2
 * Output: 24
 * Explanation: The subset chosen is the first, second, and fourth item.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= values.length == labels.length <= 20000
 * 0 <= values[i], labels[i] <= 20000
 * 1 <= num_wanted, use_limit <= values.length
 *
 *
 *
 *
 *
 */
using namespace std;
using pii = pair<int, int>;
using namespace std;
using vpii = vector<pair<int, int>>;
#define each(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
#define fori(n) for (int i = 0; i <= int(n); ++i)    // [0, n)
#include <cassert>
#define mp make_pair
#define pb push_back
#define dsize(v) (int)v.size()
#define dsort(v) sort(v.begin(), v.end())
#define rdsort(v) sort(v.rbegin(), v.rend())

class Solution {
public:
  int largestValsFromLabels(vector<int> &v, vector<int> &l, int m, int mx) {
    vpii cs;
    each(i, dsize(v) - 1) cs.pb(mp(v[i], l[i]));
    rdsort(cs);

    int res = 0, cnt = m, sz[20001] = {};
    each(i, dsize(v) - 1) if (cnt && sz[cs[i].second] < mx) sz[cs[i].second]++,
        res += cs[i].first, cnt--;
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
