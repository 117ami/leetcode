// https://leetcode.com/problems/maximum-profit-in-job-scheduling
// Hard (Difficulty)

// We have n jobs, where every job is scheduled to be done from startTime[i] to
// endTime[i], obtaining a profit of profit[i]. You're given
// the startTime , endTime and profit arrays, you need to output the maximum
// profit you can take such that there are no 2 jobs in the subset with
// overlapping time range. If you choose a job that ends at time X you will be
// able to start another job that starts at time X.   Example 1:
//
// Example 2:
//
// Example 3:
//
//  
// Constraints:
// Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
// Output: 120
// Explanation: The subset chosen is the first and fourth job.
// Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
//
//
// Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit =
// [20,20,100,70,60] Output: 150 Explanation: The subset chosen is the first,
// fourth and fifth job. Profit obtained 150 = 20 + 70 + 60.
//
// Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
// Output: 6
//
// xxxxxxxxxx
// class Solution {
// public:
//     int jobScheduling(vector<int>& startTime, vector<int>& endTime,
//  vector<int>& profit) {            }
// };
class Solution {
public:
  int jobScheduling(vector<int> &st, vector<int> &et, vector<int> &p) {
    
    vector<vector<int>> jobs;
    for (size_t i = 0; i < st.size(); i++) {
      jobs.push_back(vector<int>{st[i], et[i], p[i]});
    }
    sort(
        jobs.begin(), jobs.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[0] < b[0]; });

    int ans = 0;

    priority_queue<pair<int, int>> pq;
    static int imax = 1e6;

    for (auto &j : jobs) {
      while (!pq.empty() && pq.top().first >= imax - j[0]) {
        ans = max(ans, pq.top().second);
        pq.pop();
      }
      pq.push(pair<int, int>{imax - j[1], ans + j[2]});
    }

    while (!pq.empty()) {
      ans = max(ans, pq.top().second);
      pq.pop();
    }
    return ans;
  }
};