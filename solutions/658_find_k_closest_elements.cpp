#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**

   Given a sorted array, two integers k and x, find the k closest elements to x
in the array.  The result should also be sorted in ascending order. If there is
a tie,  the smaller elements are always preferred. Example 1: Input:
[1,2,3,4,5], k=4, x=3 Output: [1,2,3,4] Example 2: Input: [1,2,3,4,5], k=4, x=-1
   Output: [1,2,3,4]
   Note:
   The value k is positive and will always be smaller than the length of the
sorted array. Length of the given array is positive and will not exceed 104
   Absolute value of elements in the array and x will not exceed 1046
   UPDATE (2017/9/19):
   The arr parameter had been changed to an array of integers (instead of a list
of integers). Please reload the code definition to get the latest changes.

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> findClosestElements(vector<int> &arr, int k, int x) {
    int index = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
    int i = index - 1, j = index;
    while (k--)
      (i < 0 || (j < arr.size() && abs(arr[i] - x) > abs(arr[j] - x))) ? j++
                                                                       : i--;
    return vector<int>(arr.begin() + i + 1, arr.begin() + j);
  }
};

int main() {
  Solution s;
  vector<int> arr = {1, 3, 4, 7, 9, 18, 27, 82, 23, 16};
  sort(arr.begin(), arr.end());

  cout << lower_bound(arr.begin(), arr.end(), 2) - arr.begin() << endl;

}
