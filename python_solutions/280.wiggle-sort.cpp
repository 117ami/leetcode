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
  void wiggleSort(vector<int> &nums) {
    if (nums.empty()) return;

    bool less = true;
    for (int i = 0; i < nums.size() - 1; i++) {
      if ((less && (nums[i] > nums[i + 1])) || (!less && (nums[i] < nums[i + 1]))) swap(nums[i], nums[i + 1]);
      less = !less;
    }
    say(nums);
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 2, 3, 4, 5, 6};
  nums = {3, 3, 3, 3, 5, 6, 8};
  s.wiggleSort(nums);
}