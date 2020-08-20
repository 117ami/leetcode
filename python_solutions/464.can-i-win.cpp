#include <vector>
/*
 * @lc app=leetcode id=464 lang=cpp
 *
 * [464] Can I Win
 *
 * https://leetcode.com/problems/can-i-win/description/
 *
 * algorithms
 * Medium (28.83%)
 * Total Accepted:    52.4K
 * Total Submissions: 181.6K
 * Testcase Example:  '10\n11'
 *
 * In the "100 game" two players take turns adding, to a running total, any
 * integer from 1 to 10. The player who first causes the running total to reach
 * or exceed 100 wins.
 *
 * What if we change the game so that players cannot re-use integers?
 *
 * For example, two players might take turns drawing from a common pool of
 * numbers from 1 to 15 without replacement until they reach a total >= 100.
 *
 * Given two integers maxChoosableInteger and desiredTotal, return true if the
 * first player to move can force a win, otherwise return false. Assume both
 * players play optimally.
 *
 *
 * Example 1:
 *
 *
 * Input: maxChoosableInteger = 10, desiredTotal = 11
 * Output: false
 * Explanation:
 * No matter which integer the first player choose, the first player will lose.
 * The first player can choose an integer from 1 up to 10.
 * If the first player choose 1, the second player can only choose integers
 * from 2 up to 10.
 * The second player will win by choosing 10 and get a total = 11, which is >=
 * desiredTotal.
 * Same with other integers chosen by the first player, the second player will
 * always win.
 *
 *
 * Example 2:
 *
 *
 * Input: maxChoosableInteger = 10, desiredTotal = 0
 * Output: true
 *
 *
 * Example 3:
 *
 *
 * Input: maxChoosableInteger = 10, desiredTotal = 1
 * Output: true
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= maxChoosableInteger <= 20
 * 0 <= desiredTotal <= 300
 *
 *
 */
class Solution {
public:
  bool canIWin(int M, int T) {
    int sum = M * (M + 1) / 2; // sum of entire choosable pool

    // I just pick 1 to win
    if (T < 2)
      return true;

    // Total is too large, nobody can win
    else if (sum < T)
      return false;

    // Total happens to match sum, whoever picks at odd times wins
    else if (sum == T)
      return M % 2;

    // Non-trivial case: do DFS
    // Initial total: T
    // Initial game state: k = 0 (all numbers are not picked)
    else
      return dfs(M, T, 0);
  }

  // DFS to check if I can win
  // k: current game state
  // T: remaining total to reach
  bool dfs(int M, int T, int k) {
    // memorized
    if (mem[k] != 0)
      return mem[k] > 0;

    // total is already reached by opponent, so I lose
    if (T <= 0)
      return false;

    // try all currently available numbers
    for (int i = 0; i < M; ++i)
      // if (i+1) is available to pick and my opponent can't win after I picked,
      // I win!
      if (!(k & (1 << i)) && !dfs(M, T - i - 1, k | (1 << i))) {
        mem[k] = 1;
        return true;
      }

    // Otherwise, I will lose
    mem[k] = -1;
    return false;
  }

  // m[key]: memorized game result when pool state = key
  // 0: un-computed; 1: I win; -1: I lose
  int mem[1 << 20] = {};
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
