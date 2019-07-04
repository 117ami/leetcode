#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given the root node of a binary search tree (BST) and a value. You need to find
the node in the BST that the node's value equals the given value. Return the
subtree rooted with that node. If such node doesn't exist, you should return
NULL. For example, Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to search: 2
You should return this subtree:
      2
     / \
    1   3
In the example above, if we want to search the value 5, since there is no node
with value 5, we should return NULL.
 **/
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  TreeNode *searchBST(TreeNode *root, int val) {
    while (root != nullptr && root->val != val)
      root = root->val > val ? searchBST(root->left, val)
                             : searchBST(root->right, val);
    return root;
  }
};
int main() { Solution s; }
