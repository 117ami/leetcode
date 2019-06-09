/*
 * @lc app=leetcode id=5087 lang=cpp
 *
 * [5087] Letter Tile Possibilities
 *
 * https://leetcode.com/problems/letter-tile-possibilities/description/
 *
 * algorithms
 * Medium (76.77%)
 * Total Accepted:    2K
 * Total Submissions: 2.6K
 * Testcase Example:  '"AAB"'
 *
 * You have a set of tiles, where each tile has one letter tiles[i] printed on
 * it.  Return the number of possible non-empty sequences of letters you can
 * make.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: "AAB"
 * Output: 8
 * Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
 * "ABA", "BAA".
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "AAABBC"
 * Output: 188
 *
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= tiles.length <= 7
 * tiles consists of uppercase English letters.
 *
 *
 */
using namespace std;
using VI = vector<int>;
using LL = long long;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)

class Solution {
public:
  int numTilePossibilities(string tiles) {
    VI m(26, 0);
    for (auto &c : tiles)
      m[c - 'A'] += 1;
    return dfs(m);
  }
  
  int dfs(VI &m) {
    int sum = 0;
    EACH(i, 25) if (m[i] > 0) {
      sum += 1;
      m[i] -= 1;
      sum += dfs(m);
      m[i] += 1;
    }
    return sum;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
