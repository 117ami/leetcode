// https://leetcode.com/problems/palindrome-number
// Easy (Difficulty)

// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
// Example 1:
// Example 2:
// Example 3:
// Follow up:
// Coud you solve it without converting the integer to a string?
// Input: 121
// Output: true
// 
// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// 
// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// 
// xxxxxxxxxx
// class Solution {
// public:
//     bool isPalindrome(int x) {
//         
//     }
// };
class Solution {
public:
    bool isPalindrome(int x) {
        ios_base::sync_with_stdio(false); 
        if (x < 0) return false; 

        int y = 0, tmp = x; 
        while (tmp > 0){
            if(y > INT_MAX / 10) return false; 
            y = y * 10 + tmp % 10;
            tmp /= 10; 
        }

        return y == x; 
    }
};