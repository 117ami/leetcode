/*
 * @lc app=leetcode id=993 lang=javascript
 *
 * [993] Cousins in Binary Tree
 *
 * https://leetcode.com/problems/cousins-in-binary-tree/description/
 *
 * algorithms
 * Easy (52.75%)
 * Total Accepted:    10.3K
 * Total Submissions: 19.5K
 * Testcase Example:  '[1,2,3,4]\n4\n3'
 *
 * In a binary tree, the root node is at depth 0, and children of each depth k
 * node are at depth k+1.
 * 
 * Two nodes of a binary tree are cousins if they have the same depth, but have
 * different parents.
 * 
 * We are given the root of a binary tree with unique values, and the values x
 * and y of two different nodes in the tree.
 * 
 * Return true if and only if the nodes corresponding to the values x and y are
 * cousins.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * Input: root = [1,2,3,4], x = 4, y = 3
 * Output: false
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: root = [1,2,3,null,4], x = 2, y = 3
 * Output: false
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The number of nodes in the tree will be between 2 and 100.
 * Each node has a unique integer value from 1 to 100.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    var ans = [
        [-1, -1],
        [-2, -2]
    ];
    var trans = function(r, depth, pv) {
        if (!r) return;
        if (r.val == x || r.val == y) {
            ans = r.val == x ? [
                [depth, pv], ans[1]
            ] : [ans[0],
                [depth, pv]
            ];
            return;
        }
        trans(r.left, depth + 1, r.val);
        trans(r.right, depth + 1, r.val);
    };
    trans(root, 0, -3);
    return ans[0][0] == ans[1][0] && ans[0][1] != ans[1][1];
};