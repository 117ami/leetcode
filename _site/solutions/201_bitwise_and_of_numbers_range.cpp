#include "aux.cpp"
/**
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: [5,7]
Output: 4
Example 2:
Input: [0,1]
Output: 0

 https://leetcode.com/problems/bitwise-and-of-numbers-range/description/ 
 **/
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 

class Solution {
public:
  int rangeBitwiseAnd(int m, int n) {
    if (m == 0)
      return 0;
    return n > m ? rangeBitwiseAnd(m >> 1, n >> 1) << 1 : m;
  }
};

int main() { 
 Solution s; 
}
