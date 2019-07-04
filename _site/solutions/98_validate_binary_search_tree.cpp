#include "aux.cpp"
/**
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
        The left subtree of a node contains only nodes with keys less than the
node's key. The right subtree of a node contains only nodes with keys greater
than the node's key. Both the left and right subtrees must also be binary search
trees. Example 1: Input:
    2
   / \
  1   3
Output: true
Example 2:
    5
   / \
  1   4
    / \
   3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
            is 5 but its right child's value is 4.

 https://leetcode.com/problems/validate-binary-search-tree/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  bool isValidBST(TreeNode *root) { return bst(root, LONG_MIN, LONG_MAX); }
  bool bst(TreeNode *root, long minval, long maxval) {
    if (root == nullptr)
      return true;
    if (root->val <= minval || root->val >= maxval)
      return false;
    return bst(root->left, minval, root->val) &&
           bst(root->right, root->val, maxval);
  }
};
int main() { Solution s; }
