/*
 * @lc app=leetcode id=1478 lang=cpp
 *
 * [1478] Allocate Mailboxes
 *
 * https://leetcode.com/problems/allocate-mailboxes/description/
 *
 * algorithms
 * Hard (35.67%)
 * Total Accepted:    637
 * Total Submissions: 1.6K
 * Testcase Example:  '[1,4,8,10,20]\n3'
 *
 * Given the array houses and an integer k. where houses[i] is the location of
 * the ith house along a street, your task is to allocate k mailboxes in the
 * street.
 *
 * Return the minimum total distance between each house and its nearest
 * mailbox.
 *
 * The answer is guaranteed to fit in a 32-bit signed integer.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: houses = [1,4,8,10,20], k = 3
 * Output: 5
 * Explanation: Allocate mailboxes in position 3, 9 and 20.
 * Minimum total distance from each houses to nearest mailboxes is |3-1| +
 * |4-3| + |9-8| + |10-9| + |20-20| = 5
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: houses = [2,3,5,12,18], k = 2
 * Output: 9
 * Explanation: Allocate mailboxes in position 3 and 14.
 * Minimum total distance from each houses to nearest mailboxes is |2-3| +
 * |3-3| + |5-3| + |12-14| + |18-14| = 9.
 *
 *
 * Example 3:
 *
 *
 * Input: houses = [7,4,6,1], k = 1
 * Output: 8
 *
 *
 * Example 4:
 *
 *
 * Input: houses = [3,6,14,10], k = 4
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * n == houses.length
 * 1 <= n <= 100
 * 1 <= houses[i] <= 10^4
 * 1 <= k <= n
 * Array houses contain unique integers.
 *
 */
class Solution {
public:
int dp[101][101][101] = {};

int dfs(vector<int>& h, int i, int j, int k) {
    if (i >= h.size() || k <= 0)
        return i == h.size() && k == 0 ? 0 : INT_MAX;
    if (dp[i][j][k])
        return dp[i][j][k];
    dp[i][j][k] = dfs(h, i + 1, i + 1, k - 1); // New neighborhood

    if (dp[i][j][k] != INT_MAX) {
        int mailbox = (h[(i + j) / 2] + h[(i + j + 1) / 2]) / 2;
        for (auto p = j; p <= i; ++p)
            dp[i][j][k] += abs(mailbox - h[p]);        
    }
    return dp[i][j][k] = min(dp[i][j][k], dfs(h, i + 1, j, k)); // Continue neighborhood
}
int minDistance(vector<int>& houses, int k) {      
    sort(begin(houses), end(houses));
    return dfs(houses, 0, 0, k);
}
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
