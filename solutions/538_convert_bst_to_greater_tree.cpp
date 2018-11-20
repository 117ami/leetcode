#include "aux.cpp"
/**
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST. Example: Input: The root of a Binary
Search Tree like this:
              5
            /   \
           2     13
Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

 https://leetcode.com/problems/convert-bst-to-greater-tree/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
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
  int gv;

  TreeNode *convertBST(TreeNode *root) {
    convert(root);
    return root;
  }

  void convert(TreeNode *root) {
    if (root == nullptr)
      return;
    convert(root->right);
    root->val += gv;
    gv = root->val;
    convert(root->left);
  }
};
int main() { Solution s; }
