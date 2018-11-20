#include "aux.cpp"
/**
Given a binary tree containing digits from 0-9 only, each root-to-leaf path
could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note:A leaf is a node with no children.
Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
/ \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

 https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
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
  int sumNumbers(TreeNode *root) {
    int sum = 0;
    for (auto s : path(root))
      sum += stoi(s);
    return sum;
  }

  vector<string> path(TreeNode *root) {
    vector<string> res;
    if (!root)
      return res;
    if (!root->left && !root->right)
      return {to_string(root->val)};
    for (auto s : path(root->left))
      res.emplace_back(to_string(root->val) + s);
    for (auto s : path(root->right))
      res.emplace_back(to_string(root->val) + s);
    return res;
  }
};

int main() {
  Solution s;
  vector<int> arr = {1, 2, 3};
  TreeNode *r = arr2tree(arr);
  say(s.sumNumbers(r));
}
