/*
 * @lc app=leetcode id=1373 lang=cpp
 *
 * [1373] Maximum Sum BST in Binary Tree
 *
 * https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
 *
 * algorithms
 * Hard (42.28%)
 * Total Accepted:    5.5K
 * Total Submissions: 13.1K
 * Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
 *
 * Given a binary tree root, the task is to return the maximum sum of all keys
 * of any sub-tree which is also a Binary Search Tree (BST).
 * 
 * Assume a BST is defined as follows:
 * 
 * 
 * The left subtree of a node contains only nodes with keys less than the
 * node's key.
 * The right subtree of a node contains only nodes with keys greater than the
 * node's key.
 * Both the left and right subtrees must also be binary search trees.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
 * Output: 20
 * Explanation: Maximum sum in a valid Binary search tree is obtained in root
 * node with key equal to 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: root = [4,3,null,1,2]
 * Output: 2
 * Explanation: Maximum sum in a valid Binary search tree is obtained in a
 * single root node with key equal to 2.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root = [-4,-2,-5]
 * Output: 0
 * Explanation: All values are negatives. Return an empty BST.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: root = [2,1,3]
 * Output: 6
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: root = [5,4,8,3,null,6,3]
 * Output: 7
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * Each tree has at most 40000 nodes..
 * Each node's value is between [-4 * 10^4 , 4 * 10^4].
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = 0; 
    pair<bool, int> is_bst(TreeNode* root) {
        if (root == nullptr) return make_pair(true, 0);
        pair<bool, int> left = is_bst(root->left), right = is_bst(root->right);
        if (left.first && right.first) {
            if ( (root->left == nullptr || root->val > root->left->val) && (root->right == nullptr || root->val < root->right->val)) {
                res = max(res, root->val + left.second + right.second);
                return make_pair(true, root->val + left.second + right.second);
            }
        }
        return make_pair(false, 0);
    }

    int maxSumBST(TreeNode* root) {
        is_bst(root);
        return res ;
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
