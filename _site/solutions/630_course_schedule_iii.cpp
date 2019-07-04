#include "aux.cpp"
/**

There are n different online courses numbered from 1 to n. Each course has some
duration(course length)  t and closed on dth day. A course should be taken
continuously for t days and must be finished before or on the dth day. You will
start at the 1st day. Given n online courses represented by pairs (t,d), your
task is to find the maximal number of courses that can be taken. Example: Input:
[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]] Output: 3 Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th
day, and ready to take the next course on the 101st day. Second, take the 3rd
course, it costs 1000 days so you will finish it on the 1100th day, and ready to
take the next course on the 1101st day. Third, take the 2nd course, it costs 200
days so you will finish it on the 1300th day. The 4th course cannot be taken
now, since you will finish it on the 3300th day, which exceeds the closed date.
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

 https://leetcode.com/problems/course-schedule-iii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int scheduleCourse(vector<vector<int>> &courses) {
    sort(courses.begin(), courses.end(),
         [](const vector<int> &a, const vector<int> &b) {
           return a.back() < b.back();
         });
    say(courses);
    priority_queue<int> heap;
    int cost = 0;
    for (auto pair : courses) {
      heap.push(pair[0]);
      cost += pair[0];
      if (cost > pair[1]) {
        cost -= heap.top();
        heap.pop();
      }
    }
    return heap.size();
  }
};

int main() {
  Solution s;
  vector<vector<int>> courses = {
      {100, 200}, {200, 1300}, {1000, 1250}, {2000, 3200}};
  say(s.scheduleCourse(courses));
}
