/*
 * @lc app=leetcode id=996 lang=javascript
 *
 * [996] Number of Squareful Arrays
 *
 * https://leetcode.com/problems/number-of-squareful-arrays/description/
 *
 * algorithms
 * Hard (47.67%)
 * Total Accepted:    4.3K
 * Total Submissions: 8.9K
 * Testcase Example:  '[1,17,8]'
 *
 * Given an array A of non-negative integers, the array is squareful if for
 * every pair of adjacent elements, their sum is a perfect square.
 * 
 * Return the number of permutations of A that are squareful.  Two permutations
 * A1 and A2 differ if and only if there is some index i such that A1[i] !=
 * A2[i].
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,17,8]
 * Output: 2
 * Explanation: 
 * [1,8,17] and [17,8,1] are the valid permutations.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [2,2,2]
 * Output: 1
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 12
 * 0 <= A[i] <= 1e9
 * 
 */
/**
 * @param {number[]} A
 * @return {number}
 */
var numSquarefulPerms = function(A) {
    var count = {},
        cand = {},
        ans = 0;
    for (var a of A) count[a] = a in count ? count[a] + 1 : 1;
    for (var a of A)
        for (var b of A) {
            var s = Math.floor(Math.sqrt(a + b));
            if (s * s == a + b)
                if (a in cand)
                    cand[a][b] = 1;
                else {
                    cand[a] = {}
                    cand[a][b] = 1
                }
        }
    // console.log(cand);

    var dfs = function(x, cter) {
        count[x] -= 1;
        if (cter == 0) ans += 1;
        for (var y in cand[x])
            if (count[y])
                dfs(y, cter - 1);
        count[x] += 1;
    }

    for (var a in count)
        dfs(a, A.length - 1);
    return ans;
};

var A = [1, 8, 8, 17]
console.log(numSquarefulPerms(A))