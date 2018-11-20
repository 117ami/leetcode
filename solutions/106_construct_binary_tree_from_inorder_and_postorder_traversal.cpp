#include "aux.cpp"
/**
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder =[9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7

 https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int vaal;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
    return helper(inorder, postorder, 0, inorder.size() - 1, 0,
                  postorder.size() - 1);
  }

  TreeNode *helper(vector<int> &inorder, vector<int> &postorder, int i, int j,
                   int m, int n) {
    if (j < i || n < m)
      return NULL;
    if (m == n) {
      TreeNode *root = new TreeNode(postorder[n]);
      return root;
    }
    int rval = postorder[n];
    TreeNode *root = new TreeNode(rval);
    int p = i;
    while (inorder[p] != rval)
      p++;
    root->left = helper(inorder, postorder, i, p - 1, m, m + (p - 1 - i));
    root->right = helper(inorder, postorder, p + 1, j, m + (p - i), n - 1);
    return root;
  }
};

int main() {
  Solution s;
  std::vector<int> inorder = {1, 3, 2};
  std::vector<int> postorder = {3, 2, 1};
  TreeNode *res = s.buildTree(inorder, postorder);
  printTree(res);
}
