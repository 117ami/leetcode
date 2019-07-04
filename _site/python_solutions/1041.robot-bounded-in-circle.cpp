/*
 * @lc app=leetcode id=1041 lang=cpp
 *
 * [1041] Robot Bounded In Circle
 *
 * https://leetcode.com/problems/robot-bounded-in-circle/description/
 *
 * algorithms
 * Easy (41.27%)
 * Total Accepted:    4.8K
 * Total Submissions: 11.6K
 * Testcase Example:  '"GGLLGG"'
 *
 * On an infinite plane, a robot initially stands at (0, 0) and faces north.
 * The robot can receive one of three instructions:
 * 
 * 
 * "G": go straight 1 unit;
 * "L": turn 90 degrees to the left;
 * "R": turn 90 degress to the right.
 * 
 * 
 * The robot performs the instructions given in order, and repeats them
 * forever.
 * 
 * Return true if and only if there exists a circle in the plane such that the
 * robot never leaves the circle.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: "GGLLGG"
 * Output: true
 * Explanation: 
 * The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to
 * (0,0).
 * When repeating these instructions, the robot remains in the circle of radius
 * 2 centered at the origin.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "GG"
 * Output: false
 * Explanation: 
 * The robot moves north indefinitely.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: "GL"
 * Output: true
 * Explanation: 
 * The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) ->
 * ...
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= instructions.length <= 100
 * instructions[i] is in {'G', 'L', 'R'}
 * 
 * 
 */
class Solution {
public:
    bool isRobotBounded(string instructions) {
		vector<vector<int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		int x = 0, y = 0, c = 0; 
		for(int i = 0; i < instructions.size(); i ++){
			if (instructions[i] == 'L') 
				c = (c + 3) % 4;
			else if (instructions[i] == 'R')
				c = (c + 1) % 4; 
			else
				x += dir[c].front(), 
				y += dir[c].back();
		}
		return (x == 0 && y == 0) || c > 0; 
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
