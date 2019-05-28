/*
 * @lc app=leetcode id=1054 lang=cpp
 *
 * [1054] Distant Barcodes
 *
 * https://leetcode.com/problems/distant-barcodes/description/
 *
 * algorithms
 * Medium (32.68%)
 * Total Accepted:    2.8K
 * Total Submissions: 7.8K
 * Testcase Example:  '[1,1,1,2,2,2]'
 *
 * In a warehouse, there is a row of barcodes, where the i-th barcode is
 * barcodes[i].
 *
 * Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
 * return any answer, and it is guaranteed an answer exists.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,1,1,2,2,2]
 * Output: [2,1,2,1,2,1]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [1,1,1,1,2,2,3,3]
 * Output: [1,3,1,3,2,1,2,1]
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= barcodes.length <= 10000
 * 1 <= barcodes[i] <= 10000
 *
 *
 *
 *
 *
 */

using VI = vector<int>;
using SPII = set<pair<int, int>>;
using UMII = unordered_map<int, int>;


// ==================================================

// fast IO
static auto __2333__ = []() {ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();


class Solution {
public:
  vector<int> rearrangeBarcodes(vector<int> &barcodes) {
    VI res(barcodes);
    UMII m;
    SPII s;
    for (auto &b : barcodes) ++m[b];
    for (auto it = m.begin(); it != m.end(); ++it)
      s.insert({it->second, it->first});
    int pos = 0;
    for (auto it = s.rbegin(); it != s.rend(); ++it)
      for (auto cnt = 0; cnt < it->first; ++cnt, pos += 2) {
        if (pos >= res.size())
          pos = 1;
        res[pos] = it->second;
      }

    return res;
  }
};
