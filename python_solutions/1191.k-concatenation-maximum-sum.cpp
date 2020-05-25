/*
 * @lc app=leetcode id=1191 lang=cpp
 *
 * [1191] K-Concatenation Maximum Sum
 *
 * https://leetcode.com/problems/k-concatenation-maximum-sum/description/
 *
 * algorithms
 * Medium (25.86%)
 * Total Accepted:    10.3K
 * Total Submissions: 39.9K
 * Testcase Example:  '[1,2]\n3'
 *
 * Given an integer array arr and an integer k, modify the array by repeating
 * it k times.
 * 
 * For example, if arr = [1, 2] and k = 3 then the modified array will be [1,
 * 2, 1, 2, 1, 2].
 * 
 * Return the maximum sub-array sum in the modified array. Note that the length
 * of the sub-array can be 0 and its sum in that case is 0.
 * 
 * As the answer can be very large, return the answer modulo 10^9 + 7.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,2], k = 3
 * Output: 9
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,-2,1], k = 5
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [-1,-2], k = 7
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 10^5
 * 1 <= k <= 10^5
 * -10^4 <= arr[i] <= 10^4
 * 
 * 
 */
template <class T> T qsum(const vector<T> &ns) {
  T r = 0;
  for (auto n : ns)
    r += n;
  return r;
}

const int MOD = 1000000007;
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        int cur = 0, best = 0; 
        int64_t total = accumulate(arr.begin(), arr.end(), 0); 
        for (int i = 0; i < arr.size() * min(2, k) ; i ++){
            int a = arr[i % arr.size()];
            cur = max(a, cur + a) % MOD;
            best = max(best, cur) % MOD;
        }
        return max<int64_t>({0, best, best + max(total, (int64_t) 0) * (k - 2)}) % MOD;
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
