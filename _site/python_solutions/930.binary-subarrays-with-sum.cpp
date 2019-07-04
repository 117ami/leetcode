/*
 * @lc app=leetcode id=930 lang=cpp
 *
 * [930] Binary Subarrays With Sum
 *
 * https://leetcode.com/problems/binary-subarrays-with-sum/description/
 *
 * algorithms
 * Medium (37.53%)
 * Total Accepted:    8.8K
 * Total Submissions: 23.4K
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
    int numSubarraysWithSum(vector<int>& A, int S) {
		unordered_map<int, int> c({{0, 1}}); 
		int psum = 0, res = 0; 
		for(auto n : A) {
			psum += n; 
			res += c[psum - S]; 
			c[psum] ++; 
		}
		return res; 
    }
};

static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();

// int main(int argc, char const *argv[]) {
// 	Solution s;
// 	return 0;
// }

