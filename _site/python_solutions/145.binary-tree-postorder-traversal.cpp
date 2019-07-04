/*
 * @lc app=leetcode id=145 lang=cpp
 *
 * [145] Binary Tree Postorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-postorder-traversal/description/
 *
 * algorithms
 * Hard (48.40%)
 * Total Accepted:    260K
 * Total Submissions: 536.3K
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the postorder traversal of its nodes' values.
 *
 * Example:
 *
 *
 * Input: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 *
 * Output: [3,2,1]
 *
 *
 * Follow up: Recursive solution is trivial, could you do it iteratively?
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
using LL = long long;
using VI = vector<int>;
void reverse_(VI &a) { reverse(a.begin(), a.end()); }

class Solution {
public:
  vector<int> postorderTraversal(TreeNode *root) {
    VI res;
    stack<TreeNode *> st;
    st.push(root);
    while (!st.empty()) {
      TreeNode *pt = st.top();
      st.pop();
      if (pt == nullptr)
        continue;
      res.push_back(pt->val);
      st.push(pt->left);
      st.push(pt->right);
    }
    reverse_(res);
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
