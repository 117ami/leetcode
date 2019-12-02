// https://leetcode.com/problems/hexspeak
// Easy (Difficulty)

// A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.
// Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".
//  
// Example 1:
// Example 2:
//  
// Constraints:
// Input: num = "257"
// Output: "IOI"
// Explanation:  257 is 101 in hexadecimal.
// 
// Input: num = "3"
// Output: "ERROR"
// 
// xxxxxxxxxx

class Solution {
    public: 
    string toHexspeak(string n) {
        vector<string> iset = {"A", "B", "C", "D", "E", "F", "O", "I"}; 
        string ans = "";
        long num = stol(n);

        while (num > 0) {
            long a = num / 16, b = num % 16; 
            if (b < 10 && b > 1) return "ERROR"; 
            ans = iset[(b + 6) % 16] + ans; 
            num = a; 
        }
        return ans; 
        }
};

