#include "aux.cpp"
/**

Initially on a notepad only one character 'A' is present. You can perform two
operations on this notepad for each step:
Copy All: You can copy all the characters present on the notepad (partial copy
is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the
minimum number of steps permitted. Output the minimum number of steps to get n
'A'.
Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].

 https://leetcode.com/problems/2-keys-keyboard/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int minSteps(int n) {
    if (n == 1)
      return 0;
    else if (n <= 5)
      return n;
    int k = 2;
    while (n % k != 0)
      k++;
    return k == n ? n : k + minSteps(n / k);
  }
};

int main() {
  Solution s;
  int n = 100;
  say(s.minSteps(n));
}
