#include "aux.cpp"
/**

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root. Example: Given
a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
Note:
The length of path between two nodes is represented by the number of edges
between them.

 https://leetcode.com/problems/diameter-of-binary-tree/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int diameterOfBinaryTree(TreeNode *root) {
    if (!root)
      return 0;
    return max(depth(root->left) + depth(root->right),
               max(diameterOfBinaryTree(root->left),
                   diameterOfBinaryTree(root->right)));
  }

  int depth(TreeNode *root) {
    if (!root)
      return 0;
    return 1 + max(depth(root->left), depth(root->right));
  }
};

int main() {
  Solution s;
  TreeNode *root = new TreeNode(1);
  root->right = new TreeNode(3);
  root->left = new TreeNode(2);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  say(s.diameterOfBinaryTree(root));
}
