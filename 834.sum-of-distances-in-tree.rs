/*
 * @lc app=leetcode id=834 lang=rust
 *
 * [834] Sum of Distances in Tree
 *
 * https://leetcode.com/problems/sum-of-distances-in-tree/description/
 *
 * algorithms
 * Hard (42.74%)
 * Total Accepted:    12.6K
 * Total Submissions: 29.6K
 * Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
 *
 * An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges
 * are given.
 * 
 * The ith edge connects nodes edges[i][0] and edges[i][1] together.
 * 
 * Return a list ans, where ans[i] is the sum of the distances between node i
 * and all other nodes.
 * 
 * Example 1:
 * 
 * 
 * Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
 * Output: [8,12,6,10,10,10]
 * Explanation: 
 * Here is a diagram of the given tree:
 * ⁠ 0
 * ⁠/ \
 * 1   2
 * ⁠  /|\
 * ⁠ 3 4 5
 * We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
 * equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
 * 
 * 
 * Note: 1 <= N <= 10000
 * 
 */
impl Solution {
    pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
