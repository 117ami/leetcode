/*
 * @lc app=leetcode id=687 lang=cpp
 *
 * [687] Longest Univalue Path
 *
 * https://leetcode.com/problems/longest-univalue-path/description/
 *
 * algorithms
 * Easy (33.65%)
 * Total Accepted:    57.8K
 * Total Submissions: 171.7K
 * Testcase Example:  '[5,4,5,1,1,5]'
 *
 * Given a binary tree, find the length of the longest path where each node in
 * the path has the same value. This path may or may not pass through the
 * root.
 *
 * The length of path between two nodes is represented by the number of edges
 * between them.
 *
 *
 *
 * Example 1:
 *
 * Input:
 *
 *
 * ⁠             5
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         1   1   5
 *
 *
 * Output: 2
 *
 *
 *
 * Example 2:
 *
 * Input:
 *
 *
 * ⁠             1
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         4   4   5
 *
 *
 * Output: 2
 *
 *
 *
 * Note: The given binary tree has not more than 10000 nodes. The height of the
 * tree is not more than 1000.
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
class Solution {
public:
  int longestUnivaluePath(TreeNode *root) {
    int global_max = 0;
    if (root)
      dfs(root, global_max);
    return global_max;
  }

  int dfs(TreeNode *r, int &global_max) {
    int lmax = r->left ? dfs(r->left, global_max) : 0;
    int rmax = r->right ? dfs(r->right, global_max) : 0;
    int rlmax = r->left && r->left->val == r->val ? 1 + lmax : 0;
    int rrmax = r->right && r->right->val == r->val ? 1 + rmax : 0;
    global_max = max(global_max, rlmax + rrmax);
    return max(rlmax, rrmax);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
