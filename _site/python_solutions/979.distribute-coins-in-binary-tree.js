/*
 * @lc app=leetcode id=979 lang=javascript
 *
 * [979] Distribute Coins in Binary Tree
 *
 * https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
 *
 * algorithms
 * Medium (66.33%)
 * Total Accepted:    10.3K
 * Total Submissions: 15.5K
 * Testcase Example:  '[3,0,0]'
 *
 * Given the root of a binary tree with N nodes, each node in the tree has
 * node.val coins, and there are N coins total.
 * 
 * In one move, we may choose two adjacent nodes and move one coin from one
 * node to another.  (The move may be from parent to child, or from child to
 * parent.)
 * 
 * Return the number of moves required to make every node have exactly one
 * coin.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: [3,0,0]
 * Output: 2
 * Explanation: From the root of the tree, we move one coin to its left child,
 * and one coin to its right child.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: [0,3,0]
 * Output: 3
 * Explanation: From the left child of the root, we move two coins to the root
 * [taking two moves].  Then, we move one coin from the root of the tree to the
 * right child.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: [1,0,2]
 * Output: 2
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * 
 * 
 * Input: [1,0,0,null,3]
 * Output: 4
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1<= N <= 100
 * 0 <= node.val <= N
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
 * @return {number}
 */
var distributeCoins = function(root) {
    var res = 0;
    var dfs = function(r) {
        if (r == null) return 0;
        var lv = dfs(r.left),
            rv = dfs(r.right);
        var cv = lv + rv + r.val - 1;
        res += Math.abs(cv);
        return cv;
    }
    dfs(root);
    return res;
};