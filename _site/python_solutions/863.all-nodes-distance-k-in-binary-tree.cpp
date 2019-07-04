/*
 * @lc app=leetcode id=863 lang=cpp
 *
 * [863] All Nodes Distance K in Binary Tree
 *
 * https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
 *
 * algorithms
 * Medium (47.74%)
 * Total Accepted:    23.6K
 * Total Submissions: 49.5K
 * Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
 *
 * We are given a binary tree (with root node root), a target node, and an
 * integer value K.
 *
 * Return a list of the values of all nodes that have a distance K from the
 * target node.  The answer can be returned in any order.
 *
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
 *
 * Output: [7,4,1]
 *
 * Explanation:
 * The nodes that are a distance 2 from the target node (with value 5)
 * have values 7, 4, and 1.
 *
 *
 *
 * Note that the inputs "root" and "target" are actually TreeNodes.
 * The descriptions of the inputs above are just serializations of these
 * objects.
 *
 *
 *
 *
 * Note:
 *
 *
 * The given tree is non-empty.
 * Each node in the tree has unique values 0 <= node.val <= 500.
 * The target node is a node in the tree.
 * 0 <= K <= 1000.
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
using ll = long long;
using ull = unsigned long long;
using mii = map<int, int>;
using umii = unordered_map<int, int>;
#define fori(n) for (int i = 0; i <= int(n); ++i) // [0, n)
#include <cassert>
#define mp make_pair
#define pb push_back
#define eb emplace_back
template <class K, class V> bool exist(unordered_map<K, V> &m, K key) {
  return m.find(key) != m.end();
}

class Solution {
public:
  umii m;
  vi res;

  vector<int> distanceK(TreeNode *root, TreeNode *target, int K) {
    find(root, target);
    dfs(root, target, m[root->val], K);
    return res;
  }

  void dfs(TreeNode *r, TreeNode *t, int l, int K) {
    int thislen = l;
    if (r == nullptr)
      return;
    if (exist(m, r->val))
      thislen = m[r->val];
    if (thislen == K)
      res.eb(r->val);
    dfs(r->left, t, thislen + 1, K);
    dfs(r->right, t, thislen + 1, K);
  }

  int find(TreeNode *r, TreeNode *t) {
    if (r == nullptr)
      return -1;
    if (r == t) {
      m[r->val] = 0;
      return 0;
    }

    int left = find(r->left, t);
    if (left >= 0) {
      m[r->val] = left + 1;
      return left + 1;
    }
    int right = find(r->right, t);
    if (right >= 0) {
      m[r->val] = right + 1;
      return right + 1;
    }
    return -1;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
