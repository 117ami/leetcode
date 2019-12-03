// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients
// Medium (Difficulty)

// Given two integers tomatoSlices and cheeseSlices. The ingredients of
// different burgers are as follows: Return [total_jumbo, total_small] so that
// the number of remaining tomatoSlices equal to 0 and the number of remaining
// cheeseSlices equal to 0. If it is not possible to make the remaining
// tomatoSlices and cheeseSlices equal to 0 return [].   Example 1: Example 2:
// Example 3:
// Example 4:
// Example 5:
//  
// Constraints:
// Input: tomatoSlices = 16, cheeseSlices = 7
// Output: [1,6]
// Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 =
// 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
//
// Input: tomatoSlices = 17, cheeseSlices = 4
// Output: []
// Explantion: There will be no way to use all ingredients to make small and
// jumbo burgers.
//
// Input: tomatoSlices = 4, cheeseSlices = 17
// Output: []
// Explantion: Making 1 jumbo burger there will be 16 cheese remaining and
// making 2 small burgers there will be 15 cheese remaining.
//
// Input: tomatoSlices = 0, cheeseSlices = 0
// Output: [0,0]
//
// Input: tomatoSlices = 2, cheeseSlices = 1
// Output: [0,1]
//
// xxxxxxxxxx
class Solution {
public:
  vector<int> numOfBurgers(int t, int c) {
    vector<int> ans;
    if ((t - c * 2) % 2 != 0)
      return ans;
    int a = (t - c * 2) / 2;
    int b = c - a;
    if (a < 0 || b < 0) return ans; 
    return {a, b};
  }
};
