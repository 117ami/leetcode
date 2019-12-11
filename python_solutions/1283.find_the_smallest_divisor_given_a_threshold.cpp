// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
// Medium (Difficulty)

// Given an array of integers nums and an integer threshold, we will choose a
// positive integer divisor and divide all the array by it and sum the result of
// the division. Find the smallest divisor such that the result mentioned above
// is less than or equal to threshold. Each result of division is rounded to the
// nearest integer greater than or equal to that element. (For example: 7/3 = 3
// and 10/2 = 5). It is guaranteed that there will be an answer.   Example 1:
// Example 2:
// Example 3:
//  
// Constraints:
// Input: nums = [1,2,5,9], threshold = 6
// Output: 5
// Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
// If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5
// the sum will be 5 (1+1+1+2).
//
// Input: nums = [2,3,5,7,11], threshold = 11
// Output: 3
//
// Input: nums = [19], threshold = 5
// Output: 4
//
// xxxxxxxxxx
// class Solution {
// public:
//     int smallestDivisor(vector<int>& nums, int threshold) {
//         
//     }
// };
class Solution {
public:
  int cal_sum(vector<int> &ns, int div) {
    int s = 0, i = 0, j = 0, x = 1;
    while (j < ns.size()) {
      j = upper_bound(ns.begin() + i, ns.end(), x * div) - ns.begin();
      s += (j - i) * x;
      x++;
      i = j;
    }
    return s;
  }
  int smallestDivisor(vector<int> &ns, int t) {
      ios_base::sync_with_stdio(false);
    sort(ns.begin(), ns.end());
    int lo = 1, hi = 1e6, mi;
    while (lo < hi) {
      mi = (lo + hi) / 2;
    //   say(vi{lo, mi, hi});
      if (cal_sum(ns, mi) <= t)
        hi = mi;
      else
        lo = mi + 1;
    }
    return lo;
  }
};