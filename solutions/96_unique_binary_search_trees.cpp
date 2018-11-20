#include "aux.cpp"
/**
Given n, how many structurally unique BST's (binary search trees) that store
values 1 ...n? Example: Input: 3 Output: 5 Explanation: Given n = 3, there are a
total of 5 unique BST's: 1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

 https://leetcode.com/problems/unique-binary-search-trees/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int numTrees(int n) {
    if (n <= 2)
      return n;
    vector<int> cache = {1, 1, 2};
    for (int i = 3; i <= n; i++) {
      auto tmp = 0;
      for (int j = 0; j <= i - 1; j++)
        tmp += cache[j] * cache[i - 1 - j];
      cache.push_back(tmp);
    }
    return cache.back();
  }
};

int main() {
  Solution s;
  int n = 9;
  say(s.numTrees(9));
}
