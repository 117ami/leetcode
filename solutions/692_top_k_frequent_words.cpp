#include "aux.cpp"
/**
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first. Example 1: Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input:
k = 4 Output: ["the", "is", "sunny", "day"] Explanation: "the", "is", "sunny"
and "day" are the four most frequent words, with the number of occurrence being
4, 3, 2 and 1 respectively. Note: You may assume k is always valid, 1 <= k <=
number of unique elements. Input words contain only lowercase letters. Follow
up: Try to solve it in O(n log k) time and O(n) extra space.

 https://leetcode.com/problems/top-k-frequent-words/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<string> topKFrequent(vector<string> &words, int k) {
    unordered_map<string, int> hash(0);
    for (auto w : words)
      hash[w] += 1;
    vector<pair<string, int>> buckets(hash.begin(), hash.end());
    sort(buckets.begin(), buckets.end(),
         [](pair<string, int> const &a, pair<string, int> const &b) {
           return a.second != b.second ? a.second > b.second
                                       : a.first < b.first;
         });

    vector<string> res(k, "");
    for (int i = 0; i < k; i++)
      res[i] = buckets[i].first;

    return res;
  }
};

int main() {
  Solution s;

  vector<string> words = {"day", "the", "day",   "is", "sunny", "the",
                          "the", "the", "sunny", "is", "is"};
  say(s.topKFrequent(words, 3));
}
