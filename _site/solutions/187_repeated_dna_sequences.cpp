#include "aux.cpp"
/**
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA. Write a function to find all the
10-letter-long sequences (substrings) that occur more than once in a DNA
molecule. Example: Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" Output:
["AAAAACCCCC", "CCCCCAAAAA"]

 https://leetcode.com/problems/repeated-dna-sequences/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<string> findRepeatedDnaSequences(string s) {
    vector<string> res;
    if (s.size() < 11)
      return res;
    unordered_map<string, int> um;
    for (int i = 0; i <= s.size() - 10; i++)
      um[s.substr(i, 10)]++;
    for (auto it = um.begin(); it != um.end(); it++)
      if (it->second > 1)
        res.push_back(it->first);
    return res;
  }
};

int main() {
  Solution s;
  string ss = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
  ss = "AAAAAAAAAAA";
  say(s.findRepeatedDnaSequences(ss));
}
