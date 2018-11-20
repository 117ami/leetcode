#include "aux.cpp"
/**

Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by
the subtree rooted at that node (including the node itself). So what is the most
frequent subtree sum value? If there is a tie, return all the values with the
highest frequency in any order.
Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in
any order.
Examples 2
Input:
  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note:
You may assume the sum of values in any subtree is in the range of 32-bit signed
integer.

 https://leetcode.com/problems/most-frequent-subtree-sum/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  vector<int> findFrequentTreeSum(TreeNode *root) {
    std::vector<int> res;
    unordered_map<int, int> freq;
    treesum(root, freq);
    int xtp = 0;
    for (auto it = freq.begin(); it != freq.end(); it++)
      xtp = max(xtp, it->second);

    for (auto it = freq.begin(); it != freq.end(); it++)
      if (xtp == it->second)
        res.push_back(it->first);

    return res;
  }

  int treesum(TreeNode *root, unordered_map<int, int> &freq) {
    if (root == nullptr)
      return 0;
    int res =
        root->val + treesum(root->left, freq) + treesum(root->right, freq);
    freq[res]++;
    return res;
  }
};

int main() {
  Solution s;
  TreeNode *root = new TreeNode(5);
  root->left = new TreeNode(2);
  root->right = new TreeNode(-3);
  say(s.findFrequentTreeSum(root));
}
