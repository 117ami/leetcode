#include "aux.cpp"
/**
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it. Note: You may assume k is always valid, 1 <= k <= BST's
total elements. Example 1: Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
  2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest
routine?

 https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  unordered_set<int> values;
  int kthSmallest(TreeNode *root, int k) {
    traverse(root);
    vector<int> res(values.begin(), values.end());
    sort(res.begin(), res.end());
    return res[k - 1];
  }

  void traverse(TreeNode *root) {
    if (root == nullptr)
      return;
    values.insert(root->val);
    traverse(root->left);
    traverse(root->right);
  }
};

int main() { Solution s; }
