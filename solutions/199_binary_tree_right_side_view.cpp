#include "aux.cpp"
/**
Given a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom. Example:
Input:[1,2,3,null,5,null,4]
Output:[1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

 https://leetcode.com/problems/binary-tree-right-side-view/
 **/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  vector<int> rightSideView(TreeNode *root) {
    vector<int> res;
    tranversal(root, 1, res);
    return res;
  }

  void tranversal(TreeNode *root, int depth, vector<int> &res) {
    if (nullptr == root)
      return;
    if (res.size() < depth)
      res.emplace_back(root->val);
    res[depth - 1] = root->val;
    tranversal(root->left, depth + 1, res);
    tranversal(root->right, depth + 1, res);
  }
};

int main() {
  Solution s;
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->right->right = new TreeNode(4);
  root->left->right = new TreeNode(5);

  say(s.rightSideView(root));
}
