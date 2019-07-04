/*
 * @lc app=leetcode id=429 lang=cpp
 *
 * [429] N-ary Tree Level Order Traversal
 *
 * https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
 *
 * algorithms
 * Easy (59.64%)
 * Total Accepted:    34.7K
 * Total Submissions: 58.1K
 * Testcase Example:
 * '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
 *
 * Given an n-ary tree, return the level order traversal of its nodes' values.
 * (ie, from left to right, level by level).
 *
 * For example, given a 3-ary tree:
 *
 *
 *
 *
 *
 *
 *
 * We should return its level order traversal:
 *
 *
 * [
 * ⁠    [1],
 * ⁠    [3,2,4],
 * ⁠    [5,6]
 * ]
 *
 *
 *
 *
 * Note:
 *
 *
 * The depth of the tree is at most 1000.
 * The total number of nodes is at most 5000.
 *
 *
 */
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using ll = long long;
using ull = unsigned long long;
using namespace std;
#include <cassert>
#define mp make_pair
#define eb emplace_back
#define pb push_back
class Solution {
public:
  vector<vector<int>> levelOrder(Node *root) {
    vvi res;
    rec(res, root, 0);
    return res;
  }

  void rec(vvi &res, Node *r, int d) {
    if (r == nullptr)
      return;
    if (d >= res.size())
      res.pb(vi{});
    res[d].pb(r->val);
    for (auto c : r->children)
      rec(res, c, d + 1);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
