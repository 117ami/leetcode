// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
// Hard (Difficulty)

// You have a pointer at index 0 in an array of size arrLen. At each step, you
// can move 1 position to the left, 1 position to the right in the array or stay
// in the same place  (The pointer should not be placed outside the array at any
// time). Given two integers steps and arrLen, return the number of ways such
// that your pointer still at index 0 after exactly steps steps. Since the
// answer may be too large, return it modulo 10^9 + 7.   Example 1: Example 2:
// Example 3:
//  
// Constraints:
// Input: steps = 3, arrLen = 2
// Output: 4
// Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
// Right, Left, Stay
// Stay, Right, Left
// Right, Stay, Left
// Stay, Stay, Stay
//
// Input: steps = 2, arrLen = 4
// Output: 2
// Explanation: There are 2 differents ways to stay at index 0 after 2 steps
// Right, Left
// Stay, Stay
//
// Input: steps = 4, arrLen = 2
// Output: 8
//
// xxxxxxxxxx
static int mod=1e9+7 ;
class Solution {
    public:
    int numWays(int n, int arrlen) {
        size_t st = min(n / 2 + 1, arrlen); 
        vector<int> pre(st + 2), cur(st + 2); 
        pre[1] = 1; 
        while (n > 0) {
            for (size_t i = 1; i <= st; i ++) 
                cur[i] = ((long)pre[i] + pre[i-1] + pre[i+1]) % mod; 
            swap(pre, cur);
            n -- ;
        }
        return pre[1];
    }
};

// static int mod = 1e9+7; 

// class Solution {
// public:
//   vector<vector<int>> memo;
//   int arrLen;
//   int dp(int i, int steps) {
//     if (steps == 0 && i == 0) // Base condition
//       return 1;
//     if (i < 0 || i >= arrLen || steps == 0 || i > steps) // Pruning.
//       return 0;
//     if (memo[i][steps] != -1) // If we have already cached the result for
//                               // current `steps` and `index` get it.
//       return memo[i][steps];

//     memo[i][steps] = ((dp(i + 1, steps - 1) % mod + dp(i - 1, steps - 1)) % mod +
//                 dp(i, steps - 1)) %
//                mod; // Either move right, left or stay.
//     return memo[i][steps];
//   }

//   int numWays(int steps, int arrLen) {
//     memo.resize(steps / 2 + 1, vector<int>(steps + 1, -1));
//     this->arrLen = arrLen;
//     return dp(0, steps);
//   }
// };