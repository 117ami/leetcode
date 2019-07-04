#include<stdio.h>
#include<map>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
/**
   Given a binary array, find the maximum number of consecutive 1s in this array.
   Example 1:
   Input: [1,1,0,1,1,1]
   Output: 3
   Explanation: The first two digits or the last three digits are consecutive 1s.
   The maximum number of consecutive 1s is 3.
   Note:
   The input array will only contain 0 and 1.
   The length of input array is a positive integer and will not exceed 10,000

**/
using namespace std; 

static int speed_up = []() { std::ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 

class Solution {
public:
  int findMaxConsecutiveOnes(vector<int>& nums) {
    if (nums.empty()) return 0;
    int ans = 0, aux = 0;
    for(n:nums) 
      if (n==1){
	aux ++;
	ans = max(ans, aux); 
      } else {
	aux = 0; 
      }
    return ans; 
  }
};

int main() { 
  Solution s; 
}
