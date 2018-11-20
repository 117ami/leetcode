#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.
According to the definition of LCA on Wikipedia: &ldquo;The lowest common
ancestor is defined between two nodes p and qas the lowest node in T that has
both p and qas descendants (where we allow a node to be a descendant of
itself).&rdquo;
Given binary search tree: root =[6,2,8,0,4,7,9,null,null,3,5]
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself
             according to the LCA definition.
Note:
        All of the nodes' values will be unique.
        p and q are different and both values willexist in the BST.

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
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    if (root->val > p->val && root->val > q->val)
      return lowestCommonAncestor(root->left, p, q);
    else if (root->val < p->val && root->val < q->val)
      return lowestCommonAncestor(root->right, p, q);
    else
      return root;
  }
};

int main() { Solution s; }
