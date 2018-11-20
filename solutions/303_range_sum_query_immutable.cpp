#include<stdio.h>
#include<map>
#include<unordered_map>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
/**
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

 **/
using namespace std; 

static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 

class NumArray {
public:
    NumArray(vector<int> nums) {
    	xsum.push_back(0);
        for(int n: nums)
        	xsum.push_back(n + xsum.back());
    }
    
    int sumRange(int i, int j) {
    	return xsum[j+1] - xsum[i];
    }
    private:
     vector<int> xsum; 
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */

int main() { 
 Solution s; 
}
