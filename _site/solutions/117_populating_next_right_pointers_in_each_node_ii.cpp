#include "aux.cpp"
/**
Given a binary tree
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL. Initially, all next pointers
are set to NULL. Note: You may only use constant extra space. Recursive approach
is fine, implicit stack space does not count as extra space for this problem.
Example:
Given the following binary tree,
     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

 https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
 **/

// Definition for binary tree with next pointer.
struct TreeLinkNode {
  int val;
  TreeLinkNode *left, *right, *next;
  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  void connect(TreeLinkNode *root) {
    if (!root)
      return;
    if (root->left != NULL)
      root->left->next =
          root->right != NULL ? root->right : findnext(root->next);

    if (root->right != NULL)
      root->right->next = findnext(root->next);

    connect(root->right);
    connect(root->left);
  }

  TreeLinkNode *findnext(TreeLinkNode *curr) {
    if (!curr)
      return NULL;
    if (curr->left != NULL)
      return curr->left;
    if (curr->right != NULL)
      return curr->right;
    return findnext(curr->next);
  }
};

int main() { Solution s; }
