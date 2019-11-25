/*
 * @lc app=leetcode id=1267 lang=cpp
 *
 * [1267] Count Servers that Communicate
 *
 * https://leetcode.com/problems/count-servers-that-communicate/description/
 *
 * algorithms
 * Medium (57.75%)
 * Total Accepted:    4.2K
 * Total Submissions: 7.3K
 * Testcase Example:  '[[1,0],[0,1]]'
 *
 * You are given a map of a server center, represented as a m * n integer
 * matrix grid, where 1 means that on that cell there is a server and 0 means
 * that it is no server. Two servers are said to communicate if they are on the
 * same row or on the same column.
 * 
 * Return the number of servers that communicate with any other server.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: grid = [[1,0],[0,1]]
 * Output: 0
 * Explanation: No servers can communicate with others.
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: grid = [[1,0],[1,1]]
 * Output: 3
 * Explanation: All three servers can communicate with at least one other
 * server.
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
 * Output: 4
 * Explanation: The two servers in the first row can communicate with each
 * other. The two servers in the third column can communicate with each other.
 * The server at right bottom corner can't communicate with any other
 * server.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m <= 250
 * 1 <= n <= 250
 * grid[i][j] == 0 or 1
 * 
 * 
 */
class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        size_t m = grid.size(), n = grid[0].size();
        vector<int> row(m, 0), col(n, 0); 
        int res = 0; 
        for(size_t i = 0 ; i < m ; i++)
            for (size_t j = 0; j < n; j ++) 
                if (grid[i][j] > 0) {
                    row[i] ++, col[j] ++; 
                }
        
        for(size_t i = 0 ; i < m ; i++)
            for (size_t j = 0; j < n; j ++) 
            if (grid[i][j] > 0 && (row[i] > 1 || col[j] > 1)) 
                res += 1; 
        
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
