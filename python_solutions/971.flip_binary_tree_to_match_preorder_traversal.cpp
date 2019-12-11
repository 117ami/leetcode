// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal
// Medium (Difficulty)

// Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
// A node in this binary tree can be flipped by swapping the left child and the right child of that node.
// Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
// (Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
// Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
// If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
// If we cannot do so, then return the list [-1].
//  
// Example 1:
// 
// Example 2:
// 
// Example 3:
// 
//  
// Note:
// Input: root = [1,2], voyage = [2,1]
// Output: [-1]
// 
// Input: root = [1,2,3], voyage = [1,3,2]
// Output: [1]
// 
// Input: root = [1,2,3], voyage = [1,2,3]
// Output: []
// 
// xxxxxxxxxx
// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };
//  */
// class Solution {
// public:
//     vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
//         
//     }
// };

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
    vector<int> res; 
    size_t i = 0; 
    bool dfs(TreeNode* r, vector<int>&t) {
        if (!r) return true; 
        if(r->val != t[i++]) return false; 
        if(r->left && r->left->val != t[i]) {
            res.push_back(r->val);
            return dfs(r->right, t) && dfs(r->left, t); 
        } 
        return  dfs(r->left, t) && dfs(r->right, t); 

    }
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        if (dfs(root, voyage)) return res; 
        return vector<int>{-1};
    }
};