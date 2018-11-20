#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

There are 1000 buckets, one and only one of them contains poison, the rest are
filled with water. They all look the same. If a pig drinks that poison it will
die within 15 minutes. What is the minimum amount of pigs you need to figure out
which bucket contains the poison within one hour.
Answer this question, and write an algorithm for the follow-up general case.
Follow-up:
If there are n buckets and a pig drinking poison will die within m minutes, how
many pigs (x) you need to figure out the "poison" bucket within p minutes? There
is exact one bucket with poison.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    int pigs = 0;
    while (pow(minutesToTest / minutesToDie + 1, pigs) < buckets)
      pigs++;
    return pigs;
  }
};

int main() {
  Solution s;
  int a = 10;
  int b = pow(3, 2);
  cout << a / b << endl;
  cout << b << endl;
  cout << s.poorPigs(1000, 15, 60) << endl;
}
