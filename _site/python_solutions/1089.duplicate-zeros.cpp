/*
 * @lc app=leetcode id=1089 lang=cpp
 *
 * [1089] Duplicate Zeros
 *
 * https://leetcode.com/problems/duplicate-zeros/description/
 *
 * algorithms
 * Easy (58.86%)
 * Total Accepted:    3.8K
 * Total Submissions: 6.4K
 * Testcase Example:  '[1,0,2,3,0,4,5,0]'
 *
 * Given a fixed length array arr of integers, duplicate each occurrence of
 * zero, shifting the remaining elements to the right.
 *
 * Note that elements beyond the length of the original array are not written.
 *
 * Do the above modifications to the input array in place, do not return
 * anything from your function.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,0,2,3,0,4,5,0]
 * Output: null
 * Explanation: After calling your function, the input array is modified to:
 * [1,0,0,2,3,0,0,4]
 *
 *
 * Example 2:
 *
 *
 * Input: [1,2,3]
 * Output: null
 * Explanation: After calling your function, the input array is modified to:
 * [1,2,3]
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= arr.length <= 10000
 * 0 <= arr[i] <= 9
 *
 */
// using namespace std;
// using ll = long long;
// using ull = unsigned long long;
// using namespace std;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
// #define fori(n) for (int i = 0; i <= int(n); ++i)    // [0, n)
// #include <cassert>
// #define mp make_pair

class Solution {
public:
  void duplicateZeros(vector<int> &arr) {
    int m = arr.size(), idx = -1, jdx = 0;
    EACH(i, m - 1) {
      idx += arr[i] == 0 ? 2 : 1;
      jdx = i;
      if (idx >= m - 1)
        break;
    }

    // say(vi{idx,jdx});
    if (idx >= m){
    	arr[idx-1] = 0; 
	    idx -= 2;
	    jdx -= 1;
    }
    while (idx > -1) {
      if (arr[jdx] == 0) {
        arr[idx] = 0, arr[idx - 1] = 0;
        idx -= 2;
      } else {
        arr[idx] = arr[jdx];
        idx -= 1;
      }
      jdx -= 1;
    }
    // say(arr);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
