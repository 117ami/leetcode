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
Consider all the leaves of a binary tree.  From left to right order, the values
of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is the
same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
 **/
using namespace std;

// * Definition for a binary tree node.
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
  bool leafSimilar(TreeNode *root1, TreeNode *root2) {
    vector<int> va;
    vector<int> vb;
    search_leaf_nodes(root1, va);
    search_leaf_nodes(root2, vb);
    if (va.size() != vb.size())
      return false;
    for (int i = 0; i < va.size(); i++)
      if (va[i] != vb[i])
        return false;
    return true;
  }

  void search_leaf_nodes(TreeNode *root, std::vector<int> &v) {
    if (!root)
      return;

    search_leaf_nodes(root->left, v);

    if (!root->left && !root->right)
      v.push_back(root->val);

    search_leaf_nodes(root->right, v);
  }
};

int main() {
  Solution s;
  TreeNode *ra = new TreeNode(1);
  TreeNode *rb = new TreeNode(2);
  say(s.leafSimilar(ra, rb));
}
