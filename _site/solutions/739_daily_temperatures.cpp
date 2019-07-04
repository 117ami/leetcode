#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**

Given a list of daily temperatures, produce a list that, for each day in the
input, tells you how many days you would have to wait until a warmer
temperature.  If there is no future day for which this is possible, put 0
instead.
For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    vector<int> warmer(temperatures.size());
    warmer[warmer.size() - 1] = 0;
    for (int i = warmer.size() - 2; i > -1; i--) {
      int j = i + 1;
      while (j < temperatures.size() && temperatures[j] <= temperatures[i]) {
        if (warmer[j] > 0)
          j += warmer[j];
        else
          j = temperatures.size();
      }
      if (j < temperatures.size())
        warmer[i] = j - i;
    }
    return warmer;
  }
};

int main() {
  Solution s;
  vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
  for (int i : s.dailyTemperatures(temperatures))
    cout << i << " ";
  cout << endl;
}
