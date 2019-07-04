/*
 * @lc app=leetcode id=744 lang=cpp
 *
 * [744] Find Smallest Letter Greater Than Target
 *
 * https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
 *
 * algorithms
 * Easy (44.11%)
 * Total Accepted:    42.6K
 * Total Submissions: 96.5K
 * Testcase Example:  '["c","f","j"]\n"a"'
 *
 *
 * Given a list of sorted characters letters containing only lowercase letters,
 * and given a target letter target, find the smallest element in the list that
 * is larger than the given target.
 *
 * Letters also wrap around.  For example, if the target is target = 'z' and
 * letters = ['a', 'b'], the answer is 'a'.
 *
 *
 * Examples:
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "a"
 * Output: "c"
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "c"
 * Output: "f"
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "d"
 * Output: "f"
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "g"
 * Output: "j"
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "j"
 * Output: "c"
 *
 * Input:
 * letters = ["c", "f", "j"]
 * target = "k"
 * Output: "c"
 *
 *
 *
 * Note:
 *
 * letters has a length in range [2, 10000].
 * letters consists of lowercase letters, and contains at least 2 unique
 * letters.
 * target is a lowercase letter.
 *
 *
 */
using namespace std;
using ll = long long;
using namespace std;
#include <tuple>
#define fori(n) for (int i = 0; i <= int(n); ++i) // [0, n)
#include <cassert>
#define mp make_pair
#define dall(v) v.begin(), v.end()

class Solution {
public:
  char nextGreatestLetter(vector<char> &letters, char target) {
    auto it = upper_bound(dall(letters), target);
    return it == letters.end() ? letters[0] : *it;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
