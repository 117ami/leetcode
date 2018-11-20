#include "aux.cpp"
/**
Given the root node of a binary search tree (BST) and a value to be inserted
into the tree,insert the value into the BST. Return the root node of the BST
after the insertion. It is guaranteed that the new value does not exist in the
original BST. Note that there may existmultiple valid ways for theinsertion, as
long as the tree remains a BST after insertion. You can return any of them. For
example, Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \
    1   3
         \
          4

 https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
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
  TreeNode *insertIntoBST(TreeNode *root, int val) {
    if (root == nullptr) {
      TreeNode *newr = new TreeNode(val);
      return newr;
    }

    if (val > root->val) {
      root->right = insertIntoBST(root->right, val);
    } else
      root->left = insertIntoBST(root->left, val);
    return root;
  }
};

int main() { Solution s; }
