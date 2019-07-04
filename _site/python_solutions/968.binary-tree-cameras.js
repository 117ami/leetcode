/*
 * @lc app=leetcode id=968 lang=javascript
 *
 * [968] Binary Tree Cameras
 *
 * https://leetcode.com/problems/binary-tree-cameras/description/
 *
 * algorithms
 * Hard (34.96%)
 * Total Accepted:    5.7K
 * Total Submissions: 16.4K
 * Testcase Example:  '[0,0,null,0,0]'
 *
 * Given a binary tree, we install cameras on the nodes of the tree. 
 * 
 * Each camera at a node can monitor its parent, itself, and its immediate
 * children.
 * 
 * Calculate the minimum number of cameras needed to monitor all nodes of the
 * tree.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * Input: [0,0,null,0,0]
 * Output: 1
 * Explanation: One camera is enough to monitor all nodes if placed as
 * shown.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [0,0,null,0,null,0,null,null,0]
 * Output: 2
 * Explanation: At least two cameras are needed to monitor all nodes of the
 * tree. The above image shows one of the valid configurations of camera
 * placement.
 * 
 * 
 * 
 * Note:
 * 
 * 
 * The number of nodes in the given tree will be in the range [1, 1000].
 * Every node has value 0.
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
var minCameraCover = function(root) {
    var res = 0;
    var dfs = function(r) {
        if (r == null) return 'covered';
        var lv = dfs(r.left),
            rv = dfs(r.right);
        if (lv == 'leaf' || rv == 'leaf') {
            res += 1;
            return 'installed';
        }
        return (lv == 'installed' || rv == 'installed') ? 'covered' : 'leaf';
    }
    let x = dfs(root) == 'leaf' ? 1 : 0;
    return x + res;
};