/*
 * @lc app=leetcode id=927 lang=cpp
 *
 * [927] Three Equal Parts
 *
 * https://leetcode.com/problems/three-equal-parts/description/
 *
 * algorithms
 * Hard (33.58%)
 * Total Accepted:    7.3K
 * Total Submissions: 21.8K
 * Testcase Example:  '[1,0,1,0,1]'
 *
 * Given an array A of 0s and 1s, divide the array into 3 non-empty parts such
 * that all of these parts represent the same binary value.
 *
 * If it is possible, return any [i, j] with i+1 < j, such that:
 *
 *
 * A[0], A[1], ..., A[i] is the first part;
 * A[i+1], A[i+2], ..., A[j-1] is the second part, and
 * A[j], A[j+1], ..., A[A.length - 1] is the third part.
 * All three parts have equal binary value.
 *
 *
 * If it is not possible, return [-1, -1].
 *
 * Note that the entire part is used when considering what binary value it
 * represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also,
 * leading zeros are allowed, so [0,1,1] and [1,1] represent the same
 * value.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,0,1,0,1]
 * Output: [0,3]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [1,1,0,1,1]
 * Output: [-1,-1]
 *
 *
 *
 *
 * Note:
 *
 *
 * 3 <= A.length <= 30000
 * A[i] == 0 or A[i] == 1
 *
 *
 *
 *
 *
 */
class Solution {
public:
  vector<int> threeEqualParts(vector<int> &a) {
    size_t n = a.size();
    int sum = std::accumulate(a.begin(), a.end(), 0);

    if (sum % 3 > 0)
      return {-1, -1};
    if (sum == 0)
      return {0, (int)n - 1};

    int i = n - 1, j, k;
    int cnt = 0, idx_2;
    while (cnt < sum / 3) {
      if (a[i--] == 1)
        cnt++;
    }
    j = i, idx_2 = ++i;
    cnt = 0;
    while (cnt < sum / 3) {
      if (a[j--] == 1)
        cnt++;
    }
    j++;
    while (a[k++] == 0);

    while (i < n) {
      if (a[i] != a[j] || a[i] != a[k])
        return {-1, -1};
      i++, j++, k++;
    }

    return {k - 1, j};
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
