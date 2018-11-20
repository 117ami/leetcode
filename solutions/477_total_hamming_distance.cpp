#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**
   The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.
   Now your job is to find the total Hamming distance between all pairs of the
given numbers.
   Example:
   Input: 4, 14, 2
   Output: 6
   Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
0010 (just
   showing the four bits relevant in this case). So the answer will be:
   HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
2 + 2 = 6.
   Note:
   Elements of the given array are in the range of 0  to 10^9
   Length of the array will not exceed 10^4.

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int totalHammingDistance(vector<int> &nums) {
    int size = nums.size(), res = 0, *zeroCounter = new int[2];

    for (int i = 0; i < 32; i++) {
      zeroCounter[0] = zeroCounter[1] = 0;
      for (int j = 0; j < size; j++) {
        zeroCounter[nums[j] & 1]++;
        // int kkk =  nums[j] & 1;
        nums[j] >>= 1;
        // cout << j << ", " << zeroCounter[0] << ", " << kkk << "," <<
        // zeroCounter[1] << endl;
      }

      res += (zeroCounter[0] * zeroCounter[1]);
      // cout << i << ", " << res << ", " << zeroCounter[0] << ", " <<
      // zeroCounter[1] << endl;
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums{1, 2, 3};
  cout << "The answer is : " << s.totalHammingDistance(nums) << endl;
  int p = 4 ^ 14;
  for (p = 1; p < 10; p++) {
    int i = p & 1;
    cout << i << " ";
  }
  cout << endl;
}
