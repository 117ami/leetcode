/*
 * @lc app=leetcode id=987 lang=cpp
 *
 * [987] Vertical Order Traversal of a Binary Tree
 *
 * https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
 *
 * algorithms
 * Medium (31.97%)
 * Total Accepted:    10.3K
 * Total Submissions: 32.2K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, return the vertical order traversal of its nodes
 * values.
 *
 * For each node at position (X, Y), its left and right children respectively
 * will be at positions (X-1, Y-1) and (X+1, Y-1).
 *
 * Running a vertical line from X = -infinity to X = +infinity, whenever the
 * vertical line touches some nodes, we report the values of the nodes in order
 * from top to bottom (decreasing Y coordinates).
 *
 * If two nodes have the same position, then the value of the node that is
 * reported first is the value that is smaller.
 *
 * Return an list of non-empty reports in order of X coordinate.  Every report
 * will have a list of values of nodes.
 *
 *
 *
 * Example 1:
 *
 *
 *
 *
 *
 * Input: [3,9,20,null,null,15,7]
 * Output: [[9],[3,15],[20],[7]]
 * Explanation:
 * Without loss of generality, we can assume the root node is at position (0,
 * 0):
 * Then, the node with value 9 occurs at position (-1, -1);
 * The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
 * The node with value 20 occurs at position (1, -1);
 * The node with value 7 occurs at position (2, -2).
 *
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: [1,2,3,4,5,6,7]
 * Output: [[4],[2],[1,5,6],[3],[7]]
 * Explanation:
 * The node with value 5 and the node with value 6 have the same position
 * according to the given scheme.
 * However, in the report "[1,5,6]", the node value of 5 comes first since 5 is
 * smaller than 6.
 *
 *
 *
 *
 *
 * Note:
 *
 *
 * The tree will have between 1 and 1000 nodes.
 * Each node's value will be between 0 and 1000.
 *
 *
 *
 *
 *
 *
 *
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

using namespace std;
using vi = vector<int>;
using vs = vector<string>;
using vvi = vector<vi>;
using ll = long long;
using ull = unsigned long long;
using namespace std;
#define each(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
#define fori(n) for (int i = 0; i <= int(n); ++i)    // [0, n)
#include <cassert>
#define mp make_pair
#define eb emplace_back
#define dall(v) v.begin(), v.end()
#define MIN(a, b) a = min(a, b)

bool compare(const vi &a, const vi &b) {
  return (a[1] < b[1]) || (a[1] == b[1] && a[2] > b[2]) ||
         (a[1] == b[1] && a[2] == b[2] && a[0] < b[0]);
};

class Solution {
public:
  void dfs(TreeNode *r, int x, int y, map<int, map<int, set<int>>> &m) {
    if (r != nullptr) {
      m[x][y].insert(r->val);
      dfs(r->left, x - 1, y + 1, m);
      dfs(r->right, x + 1, y + 1, m);
    }
  }
  vector<vector<int>> verticalTraversal(TreeNode *r,
                                        vector<vector<int>> res = {}) {
    map<int, map<int, set<int>>> m;
    dfs(r, 0, 0, m);
    for (auto itx = m.begin(); itx != m.end(); ++itx) {
      res.push_back(vector<int>());
      for (auto ity = itx->second.begin(); ity != itx->second.end(); ++ity) {
        res.back().insert(end(res.back()), begin(ity->second),
                          end(ity->second));
      }
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
