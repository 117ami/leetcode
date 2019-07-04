#include "aux.cpp"
/**
Suppose you have a random list of people standing in a queue. Each person is
described by a pair of integers (h, k), where h is the height of the person and
k is the number of people in front of this person who have a height greater than
or equal to h. Write an algorithm to reconstruct the queue.
Note:
The number of people is less than 1,100.
Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

 https://leetcode.com/problems/queue-reconstruction-by-height/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<pair<int, int>> reconstructQueue(vector<pair<int, int>> &people) {
    vector<pair<int, int>> res;
    auto comp = [](const pair<int, int> &a, const pair<int, int> &b) {
      return a.first > b.first || a.first == b.first && a.second < b.second;
    };
    sort(people.begin(), people.end(), comp);

    for (auto person : people)
      res.insert(res.begin() + person.second, person);
    return res;
  }
};

int main() {
  Solution s;
  //[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
  vector<pair<int, int>> people = {{7, 0}, {4, 4}, {7, 1},
                                   {5, 0}, {6, 1}, {5, 2}};
  for (auto person : s.reconstructQueue(people))
    cout << person.first << " " << person.second << endl;
}
