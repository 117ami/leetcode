// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
class Solution {
public:
  int newInteger(int n) {
    int64_t res = 0, base = 1;
    while (n != 0) {
      res += n % 9 * base;
      n /= 9;
      base *= 10;
    }
    return res;
  }
};

int main() {
  Solution s;
  say(s.newInteger(800000000));
}