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
  string encode(int num) {
    int len = 0;
    while (num >= (1 << len)) {
      num -= 1 << len;
      len++;
    }
    std::string res;
    for (int i = 0; i < len; i++, num >>= 1) res = to_string(num & 1) + res;
    return res;
  }
};

int main() {
  Solution s;
  say(s.encode(8));
}