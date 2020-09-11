// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
class Solution {
public:
  string baseNeg2(int N) {
    if (N == 0)
      return "0";
    for (int i = 1; i < 32; i += 2) {
      int base = 1 << i;
      if (N & base)
        N += base * 2;
    }
    // say(N);
    int j = 0;
    string res = std::bitset<32>(N).to_string();
    while (j < res.size() && res[j] == '0')
      j++;
    return res.substr(j);
  }
};

// int main() {
//   Solution s;
//   say(s.baseNeg2(2));
// }