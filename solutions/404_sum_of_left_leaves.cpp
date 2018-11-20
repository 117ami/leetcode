#include "aux.cpp"
/**
Find the sum of all left leaves in a given binary tree.
Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.

 https://leetcode.com/problems/sum-of-left-leaves/description/
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
  int sumOfLeftLeaves(TreeNode *root, string key = "right") {
    if (root == NULL)
      return 0;
    else if (root->left == NULL && root->right == NULL)
      return key == "left" ? root->val : 0;
    else
      return sumOfLeftLeaves(root->left, "left") +
             sumOfLeftLeaves(root->right, "right");
  }
};

int main() { Solution s; }
