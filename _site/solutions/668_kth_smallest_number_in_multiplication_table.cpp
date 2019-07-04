#include "aux.cpp"
/**

Nearly every one have used the Multiplication Table. But could you find out the
k-th smallest number quickly from the multiplication table?
Given the height m and the length n of a m * n Multiplication Table, and a
positive integer k, you need to return the k-th smallest number in this table.
Example 1:
Input: m = 3, n = 3, k = 5
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]

 https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int findKthNumber(int m, int n, int k) {
    int low = 1, high = m * n, mi;
    while (low < high) {
      mi = (low + high) / 2;
      if (cter(mi, m, n) >= k)
        high = mi;
      else
        low = mi + 1;
    }
    return low;
  }
  int cter(int x, int m, int n) {
    int res = 0, i = 0;
    while (++i <= m)
      res += min(n, x / i);
    return res;
  }
};

int main() {
  Solution s;
  say(s.findKthNumber(4, 5, 17));
}
