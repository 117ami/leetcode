#include "aux.cpp"
/**

Given an integer n, return 1 - n in lexicographical order.
For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
Please optimize your algorithm to use less time and space. The input size may be
as large as 5,000,000.

 https://leetcode.com/problems/lexicographical-numbers/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> lexicalOrder(int n) {
    vector<int> res(n);
    int curr = 1;
    for (int i = 0; i < n; i++) {
      res[i] = curr;
      if (curr * 10 <= n)
        curr *= 10;
      else if (curr % 10 != 9 && curr + 1 <= n)
        curr += 1;
      else {
        while (curr % 10 == 9 || curr == n)
          curr /= 10;
        curr += 1;
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  say(s.lexicalOrder(200));
}
