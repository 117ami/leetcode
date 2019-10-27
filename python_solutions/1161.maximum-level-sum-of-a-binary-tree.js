/*
 * @lc app=leetcode id=1161 lang=javascript
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
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var dfs = function(r, depth, foo) {
    if (!r) return;
    foo[depth] += r.val;
    dfs(r.left, depth + 1, foo);
    dfs(r.right, depth + 1, foo);
}

var maxLevelSum = function(root) {
    let foo = Array(10001).fill(0);
    dfs(root, 1, foo);
    let curmax = 0,
        curid = 0;
        
    for (let i = 1; i < 10001; i++)
        if (curmax < foo[i]) {
            curmax = foo[i];
            curid = i;
        }
    return curid;
};