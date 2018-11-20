#include "aux.cpp"
/**
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
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
  void flatten(TreeNode *root) {
    if (root != nullptr)
      return;
    flatten(root->left);
    flatten(root->right);
    TreeNode *xright = root->right;
    root->right = root->left;
    root->left = nullptr;

    TreeNode *cur = root;
    while (cur->right)
      cur = cur->right;
    cur->right = xright;
  }
};

int main() {
  Solution s;

  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  s.flatten(root);
}
