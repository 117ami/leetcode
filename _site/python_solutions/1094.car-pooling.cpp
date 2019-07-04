/*
 * @lc app=leetcode id=1094 lang=cpp
 *
 * [1094] Car Pooling
 *
 * https://leetcode.com/problems/car-pooling/description/
 *
 * algorithms
 * Medium (55.93%)
 * Total Accepted:    3.2K
 * Total Submissions: 5.7K
 * Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
 *
 * You are driving a vehicle that has capacity empty seats initially available
 * for passengers.  The vehicle only drives east (ie. it cannot turn around and
 * drive west.)
 *
 * Given a list of trips, trip[i] = [num_passengers, start_location,
 * end_location] contains information about the i-th trip: the number of
 * passengers that must be picked up, and the locations to pick them up and
 * drop them off.  The locations are given as the number of kilometers due east
 * from your vehicle's initial location.
 *
 * Return true if and only if it is possible to pick up and drop off all
 * passengers for all the given trips. 
 *
 *
 *
 * Example 1:
 *
 *
 * Input: trips = [[2,1,5],[3,3,7]], capacity = 4
 * Output: false
 *
 *
 *
 * Example 2:
 *
 *
 * Input: trips = [[2,1,5],[3,3,7]], capacity = 5
 * Output: true
 *
 *
 *
 * Example 3:
 *
 *
 * Input: trips = [[2,1,5],[3,5,7]], capacity = 3
 * Output: true
 *
 *
 *
 * Example 4:
 *
 *
 * Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
 * Output: true
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 * Constraints:
 *
 *
 * trips.length <= 1000
 * trips[i].length == 3
 * 1 <= trips[i][0] <= 100
 * 0 <= trips[i][1] < trips[i][2] <= 1000
 * 1 <= capacity <= 100000
 *
 *
 */
using namespace std;
using vi = vector<int>;
using ll = long long;
using namespace std;
#define each(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
#include <cassert>
#include <tuple>
#define mp make_pair

class Solution {
public:
  bool carPooling(vector<vector<int>> &trips, int capacity) {
    vi stops(1001, 0);
    for (auto t : trips)
      stops[t[1]] += t[0], stops[t[2]] -= t[0];
    each(i, 1000) {
      capacity -= stops[i];
      if (capacity < 0)
        return false;
    }
    return capacity >= 0;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
