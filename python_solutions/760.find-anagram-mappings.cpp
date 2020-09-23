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
  vector<int> anagramMappings(vector<int> &A, vector<int> &B) {
    std::unordered_map<int, std::vector<int>> cc;
    for (int i = 0; i < B.size(); i++)
      cc[B[i]].push_back(i);
    std::vector<int> res;
    for (int i = 0; i < A.size(); i++) {
      res.push_back(cc[A[i]].back());
      cc[A[i]].pop_back();
    }
    return res;
  }
};

int main() { Solution s; }