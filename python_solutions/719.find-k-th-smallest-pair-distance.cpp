/*
 * @lc app=leetcode id=719 lang=cpp
 *
 * [719] Find K-th Smallest Pair Distance
 *
 * https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
 *
 * algorithms
 * Hard (29.26%)
 * Total Accepted:    20.2K
 * Total Submissions: 69.1K
 * Testcase Example:  '[1,3,1]\n1'
 *
 * Given an integer array, return the k-th smallest distance among all the
 * pairs. The distance of a pair (A, B) is defined as the absolute difference
 * between A and B.
 *
 * Example 1:
 *
 * Input:
 * nums = [1,3,1]
 * k = 1
 * Output: 0
 * Explanation:
 * Here are all the pairs:
 * (1,3) -> 2
 * (1,1) -> 0
 * (3,1) -> 2
 * Then the 1st smallest distance pair is (1,1), and its distance is 0.
 *
 *
 *
 * Note:
 *
 * 2 .
 * 0 .
 * 1 .
 *
 *
 */
using namespace std;
using ll = long long;
#define fori(n) for (int i = 0; i <= int(n); ++i) // [0, n)
#define mp make_pair
#define dsort(v) sort(v.begin(), v.end())

class Solution {
public:
  int smallestDistancePair(vector<int> &nums, int k) {
    dsort(nums);
    int n = nums.size(), lo = 0, hi = nums.back() - nums.front();
    while (lo < hi) {
      int cter = 0, mid = (lo + hi) / 2, i = 0, j = 0;
      while (i < n) {
        while (j < n && nums[j] - nums[i] <= mid)
          j++;
        cter += j - i - 1;
        i++;
      }
      if (cter < k)
        lo = mid + 1;
      else
        hi = mid;
    }
    return lo;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
