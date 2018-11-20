#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <vector>
/**
We are given an array A of positive integers, and two positive integers L and R
(L &lt;= R).
Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least L and at most R.
Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
[3].
Note:
        L, R&nbsp; and A[i] will be an integer in the range [0, 10^9].
        The length of A will be in the range of [1, 50000].

 **/
using namespace std;

class Solution {
public:
  int numSubarrayBoundedMax(vector<int> &A, int L, int R) {
    int size = (int)A.size(), dis = 0;
    int *pa = &A[0], *pi = pa, *pe = pi + size, res = 0;
    bool valid = false;

    while (pa < pe) {
      if (*pa >= L && *pa <= R) {
        valid = true;
        res += (dis = pa - pi + 1);
      } else if (valid && *pa < L) {
        res += dis;
      } else if (*pa > R) {
        valid = false;
        (pi = pa)++;
        dis = 0;
      }
      cout << *pa << ", " << res << endl;
      pa++;
    }
    return res;
  }

  int helper(vector<int> &arr, int bound) {
    int *pa = &arr[0], *pe = pa + arr.size(), res = 0, tmp = 0;
    while (pa < pe) {
      tmp = *pa++ <= bound ? tmp + 1 : 0;
      res += tmp;
    }
    return res;
  }

  int numSubarrayBoundedMax2(vector<int> &arr, int left, int right) {
    return helper(arr, right) - helper(arr, left - 1);
  }
};

int main() {
  Solution s;
  vector<int> A{73, 55, 36, 5, 55, 14, 9, 7, 72, 52};
  cout << s.numSubarrayBoundedMax(A, 32, 69) << endl;
  cout << s.numSubarrayBoundedMax2(A, 32, 69) << endl;
}
