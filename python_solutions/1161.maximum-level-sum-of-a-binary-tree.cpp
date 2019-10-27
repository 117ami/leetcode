/*
 * @lc app=leetcode id=1161 lang=cpp
 *
 * [1161] Maximum Level Sum of a Binary Tree
 *
 * https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
 *
 * algorithms
 * Medium (70.83%)
 * Total Accepted:    15.8K
 * Total Submissions: 22.3K
 * Testcase Example:  '[1,7,0,7,-8,null,null]'
 *
 * Given the root of a binary tree, the level of its root is 1, the level of
 * its children is 2, and so on.
 * 
 * Return the smallest level X such that the sum of all the values of nodes at
 * level X is maximal.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: [1,7,0,7,-8,null,null]
 * Output: 2
 * Explanation: 
 * Level 1 sum = 1.
 * Level 2 sum = 7 + 0 = 7.
 * Level 3 sum = 7 + -8 = -1.
 * So we return the level with the maximum sum which is level 2.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The number of nodes in the given tree is between 1 and 10^4.
 * -10^5 <= node.val <= 10^5
 * 
 * 
 */
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
    int foo [10001] = {0};
    void helper(TreeNode* t, int depth) {
        if (t == nullptr) return ; 
        foo[depth] += t->val;
        helper(t->left, depth + 1); 
        helper(t->right, depth + 1);
    }

    int maxLevelSum(TreeNode* root) {
        helper(root, 0); 
        int res = 0, m = 0; 
        for (size_t i = 0; i < size(foo); i ++) 
            if (m < foo[i]) {
                m = foo[i]; 
                res = i + 1; 
            }
        return res ;
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
