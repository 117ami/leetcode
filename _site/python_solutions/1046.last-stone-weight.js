/*
 * @lc app=leetcode id=1046 lang=javascript
 *
 * [1046] Last Stone Weight
 *
 * https://leetcode.com/problems/last-stone-weight/description/
 *
 * algorithms
 * Easy (64.22%)
 * Total Accepted:    5.1K
 * Total Submissions: 7.9K
 * Testcase Example:  '[2,7,4,1,8,1]'
 *
 * We have a collection of rocks, each rock has a positive integer weight.
 * 
 * Each turn, we choose the two heaviest rocks and smash them together.
 * Suppose the stones have weights x and y with x <= y.  The result of this
 * smash is:
 * 
 * 
 * If x == y, both stones are totally destroyed;
 * If x != y, the stone of weight x is totally destroyed, and the stone of
 * weight y has new weight y-x.
 * 
 * 
 * At the end, there is at most 1 stone left.  Return the weight of this stone
 * (or 0 if there are no stones left.)
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [2,7,4,1,8,1]
 * Output: 1
 * Explanation: 
 * We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
 * we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
 * we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
 * we combine 1 and 1 to get 0 so the array converts to [1] then that's the
 * value of last stone.
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= stones.length <= 30
 * 1 <= stones[i] <= 1000
 * 
 */
/**
 * @param {number[]} stones
 * @return {number}
 */
var bisect_left = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    if (target <= nums[0]) return 0;
    if (target >= nums[nums.length - 1]) return nums.length;

    while (i < j) {
        mid = ~~((i + j) / 2);
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] < target)
            i = mid + 1;
        else
            j = mid;
    }
    return j;
}

var lastStoneWeight = function(stones) {
    var pq = [];
    stones.forEach(function(e) {
        var idx = bisect_left(pq, e);
        pq.splice(idx, 0, e);
    });

    while (pq.length > 1) {
        var diff = pq.pop() - pq.pop();
        var idx = bisect_left(pq, diff);
        pq.splice(idx, 0, diff);
    }
    // print(pq);
    if (pq.length == 0) return 0;
    return pq[0];
};

var print = function(a) {
    console.log(a);
}

stones = [2, 7, 4, 1, 8, 1]
lastStoneWeight(stones)