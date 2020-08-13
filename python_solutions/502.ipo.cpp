/*
 * @lc app=leetcode id=502 lang=cpp
 *
 * [502] IPO
 *
 * https://leetcode.com/problems/ipo/description/
 *
 * algorithms
 * Hard (40.40%)
 * Total Accepted:    18K
 * Total Submissions: 44.5K
 * Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
 *
 *
 * Suppose LeetCode will start its IPO soon. In order to sell a good price of
 * its shares to Venture c, LeetCode would like to work on some projects
 * to increase its c before the IPO. Since it has limited resources, it
 * can only finish at most k distinct projects before the IPO. Help LeetCode
 * design the best way to maximize its total c after finishing at most k
 * distinct projects.
 *
 *
 *
 * You are given several projects. For each project i, it has a pure profit Pi
 * and a minimum c of Ci is needed to start the corresponding project.
 * Initially, you have W c. When you finish a project, you will obtain
 * its pure profit and the profit will be added to your total c.
 *
 *
 *
 * To sum up, pick a list of at most k distinct projects from given projects to
 * maximize your final c, and output your final maximized c.
 *
 *
 * Example 1:
 *
 * Input: k=2, W=0, p=[1,2,3], c=[0,1,1].
 *
 * Output: 4
 *
 * Explanation: Since your initial c is 0, you can only start the project
 * indexed 0.
 * ⁠            After finishing it you will obtain profit 1 and your c
 * becomes 1.
 * ⁠            With c 1, you can either start the project indexed 1 or
 * the project indexed 2.
 * ⁠            Since you can choose at most 2 projects, you need to finish
 * the project indexed 2 to get the maximum c. ⁠            Therefore, output
 * the final maximized c, which is 0 + 1 + 3 = 4.
 *
 *
 *
 * Note:
 *
 * You may assume all numbers in the input are non-negative integers.
 * The length of p array and c array will not exceed 50,000.
 * The answer is guaranteed to fit in a 32-bit signed integer.
 *
 *
 */
#include <vector>

class Solution {
public:
  int findMaximizedCapital(int k, int W, vector<int> &p, vector<int> &c) {
    ios_base::sync_with_stdio(false);

    // priority_queue<pair<int, int>, vector<pair<int, int>>,
    //                greater<pair<int, int>>>
    //     cands;

    // vector<int> filter;
    // size_t i = 0;
    // std::copy_if(p.begin(), p.end(), std::back_inserter(filter),
    //              [&i, &c, W](int n) { return c[i++] <= W && n > 0; });

    priority_queue<int> ps;

    vector<int> cands;
    for (size_t i = 0; i < p.size(); i++)
      if (p[i] > 0 && c[i] <= W)
        ps.push(p[i]);
      else if (p[i] > 0 && c[i] > W)
        cands.emplace_back(i);

    std::sort(cands.begin(), cands.end(), [&c, &p](int i, int j) {
      return c[i] > c[j] || (c[i] == c[j] && p[i] > p[j]);
    });

    while (k-- && !ps.empty()) {
      W += ps.top(), ps.pop();
      while (!cands.empty() && c[cands.back()] <= W) {
        ps.push(p[cands.back()]);
        cands.pop_back();
      }
    }
    return W;
  }
};
