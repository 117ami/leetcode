#include "aux.cpp"
/**
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST. For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of every node never
differ by more than 1. Example: Given the sorted array: [-10,-3,0,5,9], One
possible answer is: [0,-3,9,-10,null,5], which represents the following height
balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5

 https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    if (nums.empty())
      return NULL;
    if (1 == nums.size())
      return new TreeNode(nums.front());
    return helper(nums, 0, nums.size() - 1);
  }

  TreeNode *helper(vector<int> &nums, int i, int j) {
    if (j < i)
      return NULL;
    if (j == i)
      return new TreeNode(nums[i]);
    TreeNode *root = new TreeNode(nums[(i + j) / 2]);
    root->left = helper(nums, i, (i + j) / 2 - 1);
    root->right = helper(nums, (i + j) / 2 + 1, j);
    return root;
  }
};

int main() {
  Solution s;
  vector<int> nums = {-10, -3, 0, 5, 9};
  s.sortedArrayToBST(nums);
}
