/*
 * @lc app=leetcode id=1029 lang=javascript
 *
 * [1029] Two City Scheduling
 *
 * https://leetcode.com/problems/two-city-scheduling/description/
 *
 * algorithms
 * Easy (48.82%)
 * Total Accepted:    3.2K
 * Total Submissions: 6.6K
 * Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
 *
 * There are 2N people a company is planning to interview. The cost of flying
 * the i-th person to city A is costs[i][0], and the cost of flying the i-th
 * person to city B is costs[i][1].
 * 
 * Return the minimum cost to fly every person to a city such that exactly N
 * people arrive in each city.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [[10,20],[30,200],[400,50],[30,20]]
 * Output: 110
 * Explanation: 
 * The first person goes to city A for a cost of 10.
 * The second person goes to city A for a cost of 30.
 * The third person goes to city B for a cost of 50.
 * The fourth person goes to city B for a cost of 20.
 * 
 * The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
 * interviewing in each city.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= costs.length <= 100
 * It is guaranteed that costs.length is even.
 * 1 <= costs[i][0], costs[i][1] <= 1000
 * 
 */
/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(cs) {
    cs.sort((a, b) => ((a[0] - a[1]) - (b[0] - b[1])));
    let res = 0;
    for (var i = 0; i < cs.length / 2; i++)
        res += (cs[i][0] + cs[i + Math.floor(cs.length / 2)][1]);
    return res;
};

var cs = [
    [10, 20],
    [30, 200],
    [400, 50],
    [30, 20]
];
cs = [[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]]
console.log(twoCitySchedCost(cs))