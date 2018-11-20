#include "aux.cpp"
/**
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note: Recursive solution is trivial, could you do it iteratively?
 https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// Definition for a Node.
class Node {
public:
  int val;
  vector<Node *> children;

  Node() {}

  Node(int _val, vector<Node *> _children) {
    val = _val;
    children = _children;
  }
};

class Solution {
public:
  vector<int> postorder(Node *root) {
    vector<int> res;
    helper(root, res);
    return res;
  }
  void helper(Node *root, std::vector<int> &res) {
    if (root == nullptr)
      return;
    for (auto c : root->children)
      helper(c, res);
    res.push_back(root->val);
  }
};

int main() {
  Solution s;
  Node *root = new Node(1, {});
  Node *n5 = new Node(5, {});
  Node *n2 = new Node(2, {});
  Node *n4 = new Node(4, {});
  Node *n6 = new Node(6, {});
  Node *n3 = new Node(3, {});
  n3->children = {n5, n6};
  root->children = {n3, n2, n4};
  say(s.preorder(root));
}
