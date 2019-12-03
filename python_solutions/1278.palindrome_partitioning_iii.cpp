// https://leetcode.com/problems/palindrome-partitioning-iii
// Hard (Difficulty)

// You are given a string s containing lowercase letters and an integer k. You need to :
// Return the minimal number of characters that you need to change to divide the string.
//  
// Example 1:
// Example 2:
// Example 3:
//  
// Constraints:
// Input: s = "abc", k = 2
// Output: 1
// Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
// 
// Input: s = "aabbc", k = 3
// Output: 0
// Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
// Input: s = "leetcode", k = 8
// Output: 0
// 
// xxxxxxxxxx

class Solution {
    public:
    int cost(string s, int i, int j){
        int ans = 0; 
        while (i < j) if (s[i++] != s[j--]) ans ++; 
        return ans; 
    } 

    int dfs(map<pair<int, int>, int> &memo, string s, int i, int k){
        size_t n = s.size(); 
        if (memo.find({i, k}) != memo.end()) return memo[{i, k}]; 
        if (n - i == k) return 0; 
        if (k == 1) return cost(s, i, n - 1); 
        
        int ans = n; 
        for(size_t j = i + 1; j < n - k + 2; j ++) 
            ans = min(ans, cost(s, i, j - 1) + dfs(memo, s, j, k - 1)); 
        memo[{i, k}] = ans; 
        return ans; 
    }

    int palindromePartition(string s, int k) {
        size_t n = s.size(); 
        map<pair<int, int>, int> memo; 
        return dfs(memo, s, 0, k);
    }
};
