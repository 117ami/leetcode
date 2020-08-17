#include <vector>
/*
 * @lc app=leetcode id=1419 lang=cpp
 *
 * [1419] Minimum Number of Frogs Croaking
 *
 * https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/
 *
 * algorithms
 * Medium (46.29%)
 * Total Accepted:    11.9K
 * Total Submissions: 25.8K
 * Testcase Example:  '"croakcroak"'
 *
 * Given the string croakOfFrogs, which represents a combination of the string
 * "croak" from different frogs, that is, multiple frogs can croak at the same
 * time, so multiple “croak” are mixed. Return the minimum number of different
 * frogs to finish all the croak in the given string.
 *
 * A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’
 * sequentially. The frogs have to print all five letters to finish a croak. If
 * the given string is not a combination of valid "croak" return -1.
 *
 *
 * Example 1:
 *
 *
 * Input: croakOfFrogs = "croakcroak"
 * Output: 1
 * Explanation: One frog yelling "croak" twice.
 *
 *
 * Example 2:
 *
 *
 * Input: croakOfFrogs = "crcoakroak"
 * Output: 2
 * Explanation: The minimum number of frogs is two. 
 * The first frog could yell "crcoakroak".
 * The second frog could yell later "crcoakroak".
 *
 *
 * Example 3:
 *
 *
 * Input: croakOfFrogs = "croakcrook"
 * Output: -1
 * Explanation: The given string is an invalid combination of "croak" from
 * different frogs.
 *
 *
 * Example 4:
 *
 *
 * Input: croakOfFrogs = "croakcroa"
 * Output: -1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= croakOfFrogs.length <= 10^5
 * All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
 *
 *
 */
class Solution {
public:
  int minNumberOfFrogs(string_view croakOfFrogs) {
    int c = 0, r = 0, o = 0, a = 0, k = 0, frogs = 0;
    for (auto ch : croakOfFrogs) {
      if (ch == 'c')
        c++, frogs = max(frogs, c - k);
      else if (ch == 'r')
        r++;
      else if (ch == 'o')
        o++;
      else if (ch == 'a')
        a++;
      else if (ch == 'k')
        k++;
      else
        return -1;
      say(ch);
      say(vector<int>{c, r, o, a, k});
      say(c >= r && r >= o && o >= a && o >= k);

      if (!(c >= r && r >= o && o >= a && o >= k))
        return -1;
    }
    if (c == r && r == o && o == a && a == k)
      return frogs;
    return -1;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
