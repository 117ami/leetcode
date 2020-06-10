/*
 * @lc app=leetcode id=934 lang=cpp
 *
 * [934] Shortest Bridge
 *
 * https://leetcode.com/problems/shortest-bridge/description/
 *
 * algorithms
 * Medium (46.96%)
 * Total Accepted:    23.4K
 * Total Submissions: 49.8K
 * Testcase Example:  '[[0,1],[1,0]]'
 *
 * In a given 2D binary array A, there are two islands.  (An island is a
 * 4-directionally connected group of 1s not connected to any other 1s.)
 * 
 * Now, we may change 0s to 1s so as to connect the two islands together to
 * form 1 island.
 * 
 * Return the smallest number of 0s that must be flipped.  (It is guaranteed
 * that the answer is at least 1.)
 * 
 * 
 * Example 1:
 * Input: A = [[0,1],[1,0]]
 * Output: 1
 * Example 2:
 * Input: A = [[0,1,0],[0,0,0],[0,0,1]]
 * Output: 2
 * Example 3:
 * Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
 * Output: 1
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= A.length == A[0].length <= 100
 * A[i][j] == 0 or A[i][j] == 1
 * 
 * 
 */
class Solution {
public:
    vector<int> dirs = {-1, 0, 1, 0, -1};
    pair<int, int> first_island_idx(vector<vector<int>> &a) {
        for (int i=0;i<a.size();i++)
        for (int j=0;j<a.size();j++)
        if (a[i][j] == 1) return make_pair(i, j);
        return 
    }

    void dfs (int i, int j, vector<pair<int, int>> &borders, vector<vector<int>> &a) {
        borders.push_back({i, j});
        a[i][j]=2;
        for (int i =0;i<4;i++){
            int x = i + dirs[i], y = j + dirs[i+1]; 
            if (x >= 0 && x<a.size() && y>=0 && y<a.size() && a[i][j] == 1)
            dfs(x, y, borders, a);
        }
    }

    
    int shortestBridge(vector<vector<int>>& a) {
        vector<pair<int, int>> borders; 
        pair<int, int> pii = first_island_idx(a);
        dfs(pii.first, pii.second, borders, a);
        for (int step=0; ; step++) {
            vector<pair<int, int>> tmp; 
            for(auto &b: borders){
               for (int i =0;i<4;i++){
                   int x = b.first + dirs[i], y = b.second + dirs[i+1];
                   if (x >= 0 && x<a.size() && y>=0 && y<a.size()){
                       if (a[x][y]==1) return step; 
                       else if (a[x][y]==0) {
                           a[x][y]  =2 ;
                           tmp.push_back({x, y});
                       }
                   }
               } 
            }
            borders = tmp; 
        }
        return -1;
    }
    
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
