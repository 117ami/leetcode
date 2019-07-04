#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**
   Given a binary tree, return the level order traversal of its nodes' values.
   (ie, from left to right, level by level).
   For example:
   Given binary tree [3,9,20,null,null,15,7],
   3
   / \
   9  20
   /  \
   15   7
   return its level order traversal as:
   [
   [3],
   [9,20],
   [15,7]
   ]

**/
using namespace std;

// Definition for a binary tree node.

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();


class Solution {
  vector<vector<int>> res;
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    helper(root, 0);
    return res;
  }

  void helper(TreeNode *root, int depth) {
    if (!root)
      return;
    if (res.size() == depth)
      res.push_back(vector<int>());

    res[depth].push_back(root->val);
    helper(root->left, depth + 1);
    helper(root->right, depth + 1);
  }
};
int main() { Solution s; }
