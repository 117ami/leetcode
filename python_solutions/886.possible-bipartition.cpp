/*
 * @lc app=leetcode id=886 lang=cpp
 *
 * [886] Possible Bipartition
 *
 * https://leetcode.com/problems/possible-bipartition/description/
 *
 * algorithms
 * Medium (40.63%)
 * Total Accepted:    13.2K
 * Total Submissions: 32.6K
 * Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
 *
 * Given a set of N people (numbered 1, 2, ..., N), we would like to split
 * everyone into two groups of any size.
 *
 * Each person may dislike some other people, and they should not go into the
 * same group. 
 *
 * Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
 * people numbered a and b into the same group.
 *
 * Return true if and only if it is possible to split everyone into two groups
 * in this way.
 *
 *
 *
 *
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
 * Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
 * Output: true
 * Explanation: group1 [1,4], group2 [2,3]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
 * Output: false
 *
 *
 *
 * Example 3:
 *
 *
 * Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
 * Output: false
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= N <= 2000
 * 0 <= dislikes.length <= 10000
 * 1 <= dislikes[i][j] <= N
 * dislikes[i][0] < dislikes[i][1]
 * There does not exist i != j for which dislikes[i] == dislikes[j].
 *
 *
 *
 *
 *
 */
using namespace std;
using VI = vector<int>;
using LL = long long;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)       // [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)

class Solution {
public:
  bool possibleBipartition(int N, vector<vector<int>> &dislikes) {
    VI parents(N + 1, 0);
    EACH(i, N) parents[i] = i;
    unordered_map<int, VI> m;
    for (auto &pair : dislikes) {
      m[pair[0]].push_back(pair[1]);
      m[pair[1]].push_back(pair[0]);
    }

    UP(i, 1, N) if (m.find(i) != m.end()) {
        int p1 = find(parents, i), p2 = find(parents, m[i][0]);
        if (p1 == p2)
          return false;

        UP(j, 1, m[i].size() - 1) {
          int pj = find(parents, m[i][j]);
          if (p1 == pj)
            return false;
          parents[m[i][j]] = p2;
        }
      }

    return true;
  }

  int find(VI &parents, int i) {
    while (i != parents[i])
      i = parents[i];
    parents[i] = i;
    return i;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
