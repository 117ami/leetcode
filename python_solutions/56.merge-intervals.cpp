/*
 * @lc app=leetcode id=56 lang=cpp
 *
 * [56] Merge Intervals
 *
 * https://leetcode.com/problems/merge-intervals/description/
 *
 * algorithms
 * Medium (35.48%)
 * Total Accepted:    338.7K
 * Total Submissions: 954.7K
 * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
 *
 * Given a collection of intervals, merge all overlapping intervals.
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,3],[2,6],[8,10],[15,18]]
 * Output: [[1,6],[8,10],[15,18]]
 * Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
 * [1,6].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [[1,4],[4,5]]
 * Output: [[1,5]]
 * Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 * 
 * NOTE: input types have been changed on April 15, 2019. Please reset to
 * default code definition to get new method signature.
 * 
 */
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
		vector<vector<int>> res; 
		sort(intervals.begin(), intervals.end(), [](const std::vector<int> &a, const vector<int> &b) {return a[0] < b[0] ; });
		for (auto &i: intervals) 
			if (res.size() == 0 || res[res.size() -1][1] < i[0])
				res.push_back(i); 
			else
				res[res.size()-1][1] = 	max(res[res.size()-1][1], i[1]);
		return res;		
    }
};


static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
