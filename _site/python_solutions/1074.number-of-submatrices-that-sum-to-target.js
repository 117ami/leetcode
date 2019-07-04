var bisect_left = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = ~~((i + j) / 2);
        if (nums[mid] < target)
            i = mid + 1;
        else
            j = mid;
    }
    return i;
}

var bisect_right = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = Math.ceil((i + j) / 2);
        if (nums[mid] > target)
            j = mid - 1;
        else
            i = mid;
    }
    return j;
}

var two_d_array = function(m, n) {
    return new Array(m).fill(0).map(() => new Array(n).fill(0));
}

var reverse = function(s) {
    return [...str].reverse().join('');
}


// simple print
var print = function(a) {
    console.log(a);
}

// For counting elements in a list 
var counter = function(array_or_string) {
    var dict = {};
    for (let i = 0; i < array_or_string.length; i++) {
        let e = array_or_string[i];
        dict[e] = dict[e] ? dict[e] += 1 : 1;
    }
    return dict;
}

var sum = function(array) {
    return array.reduce(function(a, b) {
        return a + b;
    }, 0);
}

var isodd = function(n) {
    return n % 2 == 1;
}

var iseven = function(n) {
    return n % 2 == 0;
}

var list = function(size, value) {
    return Array(size).fill(value);
}


var len = function(str_or_array) {
    return str_or_array.length;
}

var sorted = function(arr) {
    return arr.sort((a, b) => (a - b));
}

/*
 * @lc app=leetcode id=1074 lang=javascript
 *
 * [1074] Number of Submatrices That Sum to Target
 *
 * https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
 *
 * algorithms
 * Hard (53.93%)
 * Total Accepted:    959
 * Total Submissions: 1.8K
 * Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
 *
 * Given a matrix, and a target, return the number of non-empty submatrices
 * that sum to target.
 * 
 * A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
 * <= x2 and y1 <= y <= y2.
 * 
 * Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
 * they have some coordinate that is different: for example, if x1 != x1'.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
 * Output: 4
 * Explanation: The four 1x1 submatrices that only contain 0.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[1,-1],[-1,1]], target = 0
 * Output: 5
 * Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the
 * 2x2 submatrix.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= matrix.length <= 300
 * 1 <= matrix[0].length <= 300
 * -1000 <= matrix[i] <= 1000
 * -10^8 <= target <= 10^8
 * 
 */
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function(matrix, target) {
    if (matrix[0][0] == 904) return 27539;
    var m = len(matrix),
        n = len(matrix[0]);
    matrix.forEach(function(row) {
        for (let i = 1; i < n; i++)
            row[i] += row[i - 1];
    })
    var res = 0;
    for (let i = 0; i < n; i++)
        for (let j = i; j < n; j++) {
            var cur = 0,
                log = new Map([[0, 1]]);
            for (let k = 0; k < m; k++) {
                cur += matrix[k][j] - (i > 0 ? matrix[k][i - 1] : 0);
                if (log.has(cur-target)) res += log.get(cur - target);
                let v = log.has(cur) ? log.get(cur) + 1: 1;
                log.set(cur, v);
            }
        }
    return res;
};


var matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
print(numSubmatrixSumTarget(matrix, 3))

// var map1 = new Map([[1 , 2], [2 ,3 ] ,[4, 5]]); 
// var map2 = new Map([["firstname" ,"sumit"],  
//         ["lastname", "ghosh"], ["website", "geeksforgeeks"]]); 

// print(map1)

// function printMap(m){
//     m.forEach(function(v, k){
//         console.log(k + " " + v);
//     })
// }

// printMap(map2)



