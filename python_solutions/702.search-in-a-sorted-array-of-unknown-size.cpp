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
/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

class Solution {
public:
  int search(const ArrayReader &reader, int target) {
    int lo = 0, hi = 10001; //
    while (lo <= hi) {
      int mid = (lo + hi) / 2;
      int val = reader.get(mid);
      if (val == target)
        return mid;
      else if (val == 2147483647 || val > target)
        hi = mid - 1;
      else
        lo = mid + 1;
    }
    return -1;
  }
};

int main() { Solution s; }