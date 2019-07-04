#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**

Your task is to calculate ab mod 1337 where a is a positive integer and b is an
extremely large positive integer given in the form of an array. Example1: a = 2
b = [3]
Result: 8
Example2:
a = 2
b = [1,0]
Result: 1024
Credits:Special thanks to @Stomach_ache for adding this problem and creating all
test cases.
 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
  const int base = 1337;
  int powMod(int a, int k) {
    int res = 1;
    a %= base; // this is important, for otherwise when a is a very big number,
               // the result may overflow
    for (int i = 0; i < k; i++)
      res = (res * a) % base;
    return res;
  }

public:
  int superPow(int a, vector<int> &b) {
    if (b.empty())
      return 1;
    int b_back = b.back();
    b.pop_back();
    return powMod(a, b_back) * powMod(superPow(a, b), 10) % base;
  }
};

int main() {
  Solution s;
  vector<int> b{1, 0};
  cout << s.superPow(2, b) << endl;
}
