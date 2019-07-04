#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
/**
   Given a binary tree, find its minimum depth.
   The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
   Note:&nbsp;A leaf is a node with no children.
   Example:
   Given binary tree [3,9,20,null,null,15,7],
   3
   / \
   9  20
   /  \
   15   7
   return its minimum&nbsp;depth = 2.

**/
using namespace std; 

static int speed_up = []() { std::ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 


// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  int minDepth(TreeNode* root) {
    if (!root) return 0;
    if (!root->left) return 1 + minDepth(root->right);
    if (!root->right) return 1 + minDepth(root->left);
    return 1 + min(minDepth(root->left), minDepth(root->right));
  }
};

int main() { 
  Solution s;
}
