#include "aux.cpp"
/**
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between). For example: Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

 https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
 **/
//  Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {

public:
  // unordered_map<int, int> dc(0); // short for depth counter
  vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
    vector<vector<int>> res;
    traversal(root, 0, res);
    say(res);
    return res;
  }

  void traversal(TreeNode *r, int depth, vector<vector<int>> &res) {
    if (r == nullptr)
      return;
    if (res.begin() + depth == res.end())
      res.push_back(vector<int>(1, r->val));
    else if (0 == depth % 2)
      res[depth].push_back(r->val);
    else
      res[depth].insert(res[depth].begin(), r->val);
    traversal(r->left, depth + 1, res);
    traversal(r->right, depth + 1, res);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

int main() {
  Solution s;
  TreeNode *root = new TreeNode(3);
  root->left = new TreeNode(9);
  root->right = new TreeNode(20);
  root->right->left = new TreeNode(15);
  root->right->right = new TreeNode(7);
  s.zigzagLevelOrder(root);
}
