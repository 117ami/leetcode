/*
 * @lc app=leetcode id=896 lang=cpp
 *
 * [896] Monotonic Array
 *
 * https://leetcode.com/problems/monotonic-array/description/
 *
 * algorithms
 * Easy (54.81%)
 * Total Accepted:    37.5K
 * Total Submissions: 68.4K
 * Testcase Example:  '[1,2,2,3]'
 *
 * An array is monotonic if it is either monotone increasing or monotone
 * decreasing.
 *
 * An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
 * A is monotone decreasing if for all i <= j, A[i] >= A[j].
 *
 * Return true if and only if the given array A is monotonic.
 *
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,2,2,3]
 * Output: true
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [6,5,4,4]
 * Output: true
 *
 *
 *
 * Example 3:
 *
 *
 * Input: [1,3,2]
 * Output: false
 *
 *
 *
 * Example 4:
 *
 *
 * Input: [1,2,4,5]
 * Output: true
 *
 *
 *
 * Example 5:
 *
 *
 * Input: [1,1,1]
 * Output: true
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= A.length <= 50000
 * -100000 <= A[i] <= 100000
 *
 *
 *
 *
 *
 *
 *
 */
class Solution {
public:
  bool isMonotonic(vector<int> &A) {
    bool incre = true, decre = true;
    for (int i = 0; i < A.size() - 1; i++) {
      if (A[i] < A[i + 1])
        decre = false;
      else if (A[i] > A[i + 1])
        incre = false;
    }
    return incre || decre;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
// 	Solution s;
// 	return 0;
// }
