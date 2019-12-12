/*
 * @lc app=leetcode id=894 lang=cpp
 *
 * [894] All Possible Full Binary Trees
 *
 * https://leetcode.com/problems/all-possible-full-binary-trees/description/
 *
 * algorithms
 * Medium (72.57%)
 * Total Accepted:    26.2K
 * Total Submissions: 36.1K
 * Testcase Example:  '7'
 *
 * A full binary tree is a binary tree where each node has exactly 0 or 2
 * children.
 * 
 * Return a list of all possible full binary trees with N nodes.  Each element
 * of the answer is the root node of one possible tree.
 * 
 * Each node of each tree in the answer must have node.val = 0.
 * 
 * You may return the final list of trees in any order.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 7
 * Output:
 * [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
 * Explanation:
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= N <= 20
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
    unordered_map<int, vector<TreeNode*>> cache; 
    vector<TreeNode*> allPossibleFBT(int n) {
        if (cache.count(n) > 0) return cache[n];

        vector<TreeNode*> res ; 
        if (n == 1) {
            res.push_back(new TreeNode(0));
        }

        for (size_t i = 1; i < n; i += 2){
            for(TreeNode* l: allPossibleFBT(i)) 
                for (TreeNode* r: allPossibleFBT(n-i-1)){
                    TreeNode * root = new TreeNode(0);
                    root->left = l; 
                    root->right=r; 
                    res.push_back(root);
                }
        }
        cache[n] = res; 
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
