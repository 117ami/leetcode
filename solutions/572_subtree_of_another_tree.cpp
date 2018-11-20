#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**

   Given two non-empty binary trees s and t, check whether tree t has exactly
the same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself. Example 1: Given tree s:
   3
   / \
   4   5
   / \
   1   2
   Given tree t:
   4
   / \
   1   2
   Return true, because t has the same structure and node values with a subtree
of s. Example 2: Given tree s:
   3
   / \
   4   5
   / \
   1   2
   /
   0
   Given tree t:
   4
   / \
   1   2
   Return false.

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
public:
  bool isSubtree(TreeNode *s, TreeNode *t) {
    if (t == NULL)
      return true;
    if (s == NULL)
      return false; // t is not NULL
    return identicalTree(s, t) || isSubtree(s->left, t) ||
           isSubtree(s->right, t);
  }

  bool identicalTree(TreeNode *s, TreeNode *t) {
    if (s == NULL && t == NULL)
      return true;
    if (s == NULL && t != NULL || s != NULL && t == NULL || s->val != t->val)
      return false;
    return identicalTree(s->left, t->left) && identicalTree(s->right, t->right);
  }
};

TreeNode arrayToTreenode(vector<int> v) {}

int main() {
  Solution s;
  cout << s.isSubtree(NULL, NULL) << endl;
}
