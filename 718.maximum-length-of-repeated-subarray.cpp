/*
 * @lc app=leetcode id=718 lang=cpp
 *
 * [718] Maximum Length of Repeated Subarray
 *
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
 *
 * algorithms
 * Medium (47.47%)
 * Total Accepted:    42.6K
 * Total Submissions: 89.5K
 * Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
 *
 * Given two integer arrays A and B, return the maximum length of an subarray
 * that appears in both arrays.
 * 
 * Example 1:
 * 
 * 
 * Input:
 * A: [1,2,3,2,1]
 * B: [3,2,1,4,7]
 * Output: 3
 * Explanation: 
 * The repeated subarray with maximum length is [3, 2, 1].
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= len(A), len(B) <= 1000
 * 0 <= A[i], B[i] < 100
 * 
 * 
 * 
 * 
 */

class Solution {
public:
    int maxlen = 0; 
    void helper(vector<int>& A, vector<int>& B){
        for (int i = 0 ; i < A.size() - maxlen; i ++ ){
            int j = i, k = 0, curlen = 0; 
            while ( j < A.size() && k < B.size()) {
                if (A[j] == B[k]) maxlen = max(maxlen, ++ curlen); 
                else curlen = 0; 
                j ++; 
                k ++; 
            }
        }
    }

    int findLength(vector<int>& A, vector<int>& B) {
        int size_a = A.size(), size_b = B.size(); 
        helper(A, B); 
        helper(B, A);
        // for (int i = 0 ; i < size_a - maxlen; i ++ ){
        //     int j = i, k = 0, curlen = 0; 
        //     while ( j < size_a && k < size_b) {
        //         if (A[j] == B[k]) maxlen = max(maxlen, ++curlen); 
        //         else curlen = 0; 
        //         j ++; 
        //         k ++; 
        //     }
        // }
        // for (int i = 0; i < size_b - maxlen; i ++) {
        //     int j = 0, k = i, curlen = 0; 
        //     while ( j < size_a && k < size_b) {
        //         if (A[j] == B[k]) maxlen = max(maxlen, ++curlen); 
        //         else curlen = 0; 
        //         j ++; 
        //         k ++; 
        //     }
        // }
        return maxlen; 
    }

    int findLength2(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size(), res = 0; 
        vector<vector<int>> dp(m + 1, vector<int> (n + 1, 0)); 
        for (int i = 0; i < m; i ++) {
            for (int j = 0; j < n; j ++) {
                if (A[i] == B[j]) {
                    dp[i+1][j+1] = 1 + dp[i][j]; 
                    res = max(res, dp[i+1][j+1]); 
                }
            }
        }
        return res; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
