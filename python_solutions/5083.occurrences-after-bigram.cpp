/*
 * @lc app=leetcode id=5083 lang=cpp
 *
 * [5083] Occurrences After Bigram
 *
 * https://leetcode.com/problems/occurrences-after-bigram/description/
 *
 * algorithms
 * Easy (70.04%)
 * Total Accepted:    3.1K
 * Total Submissions: 4.4K
 * Testcase Example:  '"alice is a good girl she is a good
 * student"\n"a"\n"good"'
 *
 * Given words first and second, consider occurrences in some text of the form
 * "first second third", where second comes immediately after first, and third
 * comes immediately after second.
 *
 * For each such occurrence, add "third" to the answer, and return the
 * answer.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: text = "alice is a good girl she is a good student", first = "a",
 * second = "good"
 * Output: ["girl","student"]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: text = "we will we will rock you", first = "we", second = "will"
 * Output: ["we","rock"]
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= text.length <= 1000
 * text consists of space separated words, where each word consists of
 * lowercase English letters.
 * 1 <= first.length, second.length <= 10
 * first and second consist of lowercase English letters.
 *
 *
 *
 */
using namespace std;
using VS = vector<string>;
using LL = long long;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)

class Solution {
public:
  vector<string> findOcurrences(string text, string first, string second) {
    VS res, tmp;
    stringstream iss(text);
    string word;
    while (iss >> word)
      tmp.emplace_back(word);
    EACH(i, tmp.size() - 3)
    if (tmp[i] == first && tmp[i + 1] == second)
        res.emplace_back(tmp[i++ + 2]);
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
