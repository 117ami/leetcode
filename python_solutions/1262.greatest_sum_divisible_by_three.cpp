// https://leetcode.com/problems/greatest-sum-divisible-by-three
// Medium (Difficulty)

// Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
//  
// Example 1:
// Example 2:
// Example 3:
//  
// Constraints:
// Input: nums = [3,6,5,1,8]
// Output: 18
// Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
// Input: nums = [4]
// Output: 0
// Explanation: Since 4 is not divisible by 3, do not pick any number.
// 
// Input: nums = [1,2,3,4,4]
// Output: 12
// Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
// 
// xxxxxxxxxx


class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int r = sum % 3; 
        if (r == 0) return sum; 
        sort(nums.begin(), nums.end());
        
        vector<int> a1, a2; 
        for (auto i: nums){
            if (i % 3 == 1) a1.push_back(i); 
            if (i % 3 == 2) a2.push_back(i); 
            if (a1.size() >= 2 && a2.size() >= 2) break; 
        }

        if (r == 1) 
            return sum - (a2.size() < 2 ? a1[0] : min(a1[0], a2[0] + a2[1])); 
        else 
            return sum - (a1.size() < 2 ? a2[0] : min(a2[0], a1[0] + a1[1])); 

}
};
