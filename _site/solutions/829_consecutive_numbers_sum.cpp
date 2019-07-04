#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a positive integerN, how many ways can we write it as a sum ofconsecutive
positive integers?
Example 1:
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note:1 <= N <= 10 ^ 9.
 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int consecutiveNumbersSum(int n) {
    int count = 1;
    for (int k = 2; k < sqrt(2 * n); k++)
      if ((n - k * (k - 1) / 2) % k == 0)
        count++;
    return count;
  }
};

int main() {
  Solution s;
  for (int i = 10; i < 100; i += 1)
    cout << i << ", " << s.consecutiveNumbersSum(i) << endl;
}
