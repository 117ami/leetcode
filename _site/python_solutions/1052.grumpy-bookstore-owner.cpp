/*
 * @lc app=leetcode id=1052 lang=cpp
 *
 * [1052] Grumpy Bookstore Owner
 *
 * https://leetcode.com/problems/grumpy-bookstore-owner/description/
 *
 * algorithms
 * Medium (48.54%)
 * Total Accepted:    3K
 * Total Submissions: 6.2K
 * Testcase Example:  '[1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3'
 *
 * Today, the bookstore owner has a store open for customers.length minutes.
 * Every minute, some number of customers (customers[i]) enter the store, and
 * all those customers leave after the end of that minute.
 *
 * On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
 * grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
 * bookstore owner is grumpy, the customers of that minute are not satisfied,
 * otherwise they are satisfied.
 *
 * The bookstore owner knows a secret technique to keep themselves not grumpy
 * for X minutes straight, but can only use it once.
 *
 * Return the maximum number of customers that can be satisfied throughout the
 * day.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
 * Output: 16
 * Explanation: The bookstore owner keeps themselves not grumpy for the last 3
 * minutes.
 * The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 +
 * 5 = 16.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= X <= customers.length == grumpy.length <= 20000
 * 0 <= customers[i] <= 1000
 * 0 <= grumpy[i] <= 1
 *
 */
class Solution {
public:
  int maxSatisfied(vector<int> &c, vector<int> &g, int x) {
    int sum = accumulate(c.begin(), c.end(), 0), lost = 0, res = 0;
    
    for (int i = x; i < g.size(); i++)
      lost += g[i] * c[i];
    res = sum - lost;

    for (int i = 1; i <= c.size() - x; i++) {
      lost += c[i - 1] * g[i - 1] - c[i + x - 1] * g[i + x - 1];
      res = max(res, sum - lost);
      // cout << i << " " << lost << endl;
    }
    return res;
  }
};

static const int _ = []() {ios::sync_with_stdio(false); cin.tie(NULL); return 0;} (); 
