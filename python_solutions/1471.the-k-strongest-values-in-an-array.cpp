/*
 * @lc app=leetcode id=1471 lang=cpp
 *
 * [1471] The k Strongest Values in an Array
 *
 * https://leetcode.com/problems/the-k-strongest-values-in-an-array/description/
 *
 * algorithms
 * Medium (55.30%)
 * Total Accepted:    11.6K
 * Total Submissions: 20.3K
 * Testcase Example:  '[1,2,3,4,5]\n2'
 *
 * Given an array of integers arr and an integer k.
 * 
 * A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| >
 * |arr[j] - m| where m is the median of the array.
 * If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than
 * arr[j] if arr[i] > arr[j].
 * 
 * Return a list of the strongest k values in the array. return the answer in
 * any arbitrary order.
 * 
 * Median is the middle value in an ordered integer list. More formally, if the
 * length of the list is n, the median is the element in position ((n - 1) / 2)
 * in the sorted list (0-indexed).
 * 
 * 
 * For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the
 * array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) /
 * 2) = 2. The median is 6.
 * For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the
 * array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2)
 * = 1. The median is 3.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,2,3,4,5], k = 2
 * Output: [5,1]
 * Explanation: Median is 3, the elements of the array sorted by the strongest
 * are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also
 * accepted answer.
 * Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1
 * because 5 > 1.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,1,3,5,5], k = 2
 * Output: [5,5]
 * Explanation: Median is 3, the elements of the array sorted by the strongest
 * are [5,5,1,1,3]. The strongest 2 elements are [5, 5].
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [6,7,11,7,6,8], k = 5
 * Output: [11,8,6,6,7]
 * Explanation: Median is 7, the elements of the array sorted by the strongest
 * are [11,8,6,6,7,7].
 * Any permutation of [11,8,6,6,7] is accepted.
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: arr = [6,-3,7,2,11], k = 3
 * Output: [-3,11,2]
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: arr = [-7,22,17,3], k = 2
 * Output: [22,17]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 10^5
 * -10^5 <= arr[i] <= 10^5
 * 1 <= k <= arr.length
 * 
 */
class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        int m = arr[(arr.size()-1)>>1];
        sort(arr.begin(), arr.end(), [&](const int a, const int b){return abs(a - m) > abs(b - m) || (abs(a - m) == abs(b - m) && a > b) ;});
        return vector<int>(arr.begin(), arr.begin() + k);
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
