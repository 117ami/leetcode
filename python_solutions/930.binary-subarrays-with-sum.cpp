#include<vector>
/*
 * @lc app=leetcode id=930 lang=cpp
 *
 * [930] Binary Subarrays With Sum
 *
 * https://leetcode.com/problems/binary-subarrays-with-sum/description/
 *
 * algorithms
 * Medium (43.27%)
 * Total Accepted:    22.5K
 * Total Submissions: 52K
 * Testcase Example:  '[1,0,1,0,1]\n2'
 *
 * In an array A of 0s and 1s, how many non-empty subarrays have sum S?
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: A = [1,0,1,0,1], S = 2
 * Output: 4
 * Explanation: 
 * The 4 subarrays are bolded below:
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * [1,0,1,0,1]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * A.length <= 30000
 * 0 <= S <= A.length
 * A[i] is either 0 or 1.
 * 
 */
class Solution {
public:
    int atmost(int m, vector<int> &ns) {
        if (m<0) return 0; 
        int n = ns.size(), i = 0, cnt = 0; 
        for(int j = 0; j < n; j ++) {
            m -= ns[j]; 
            while (m < 0) m += ns[i++];
            cnt += j - i + 1; 
        }
        return cnt; 
    }

    int numSubarraysWithSum(vector<int>& A, int S) {
        return atmost(S, A)     - atmost(S-1, A);
    }
};



auto speed_up = [] () {
    ios_base::sync_with_stdio(false);
    return 0;
}(); 
