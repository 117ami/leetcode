#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
   Level up your coding skills and quickly land a job. This is the best place to
expand your knowledge and get prepared for your next interview.
**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int reachNumber(int target) {
    if (target < 0)
      return reachNumber(abs(target));
    int res = (int)sqrt(target);
    while ((res + 1) * res / 2 < target ||
           ((res + 1) * res / 2 - target) % 2 == 1)
      res++;

    return res;
  }
};

int main() {
  Solution s;
  int target = 13;
  for (int i = 1; i < 69; i++)
    cout << i << " " << s.reachNumber(i) << " ** ";
  cout << endl;
  cout << s.reachNumber(90202021) << endl;
}
